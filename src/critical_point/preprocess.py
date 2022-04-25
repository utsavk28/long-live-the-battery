import numpy as np
import pandas as pd
import os
from scipy.io import loadmat


def preprocess_data_to_cycles():
    path = "../../data/input/battery-data-set"
    dis = os.listdir(path)
    dis_mat = []
    battery_grp = {}

    for i in dis:
        filtered_list = list(filter(lambda x: x.split(
            '.')[-1] == 'mat', os.listdir(f"{path}/{i}")))
        battery_grp[i.split('BatteryAgingARC')[-1][1:]
                    ] = list(map(lambda x: x.split('.')[0], filtered_list))
        dis_mat.extend(list(map(lambda x: f"{path}/{i}/{x}", filtered_list)))

    battery_grp['5_6_7_18'] = battery_grp['FY08Q4']
    del battery_grp['FY08Q4']

    bs = [x.split('/')[-1].split('.')[0] for x in dis_mat]

    ds = []
    for b in dis_mat:
        ds.append(loadmat(b))

    types = []
    times = []
    ambient_temperatures = []
    datas = []

    for i in range(len(ds)):
        x = ds[i][bs[i]]["cycle"][0][0][0]
        ambient_temperatures.append(
            list(map(lambda y: y[0][0], x['ambient_temperature'])))
        types.append(x['type'])
        times.append(x['time'])
        datas.append(x['data'])

    batteries = []
    cycles = []
    for i in range(len(ds)):
        batteries.append(bs[i])
        cycles.append(datas[i].size)

    battery_cycle_df = pd.DataFrame(
        {'Battery': batteries, 'Cycle': cycles}).sort_values('Battery', ascending=True)
    battery_cycle_df.drop_duplicates(inplace=True)

    Cycles = {}
    params = ['Voltage_measured', 'Current_measured', 'Temperature_measured',
              'Current_load', 'Voltage_load', 'Time', 'Capacity', ]

    for i in range(len(bs)):
        Cycles[bs[i]] = {}
        Cycles[bs[i]]['count'] = 0
        for param in params:
            Cycles[bs[i]][param] = []
            for j in range(datas[i].size):
                if types[i][j] == 'discharge':
                    Cycles[bs[i]][param].append(datas[i][j][param][0][0][0])

        cap = []
        amb_temp = []
        for j in range(datas[i].size):
            if types[i][j] == 'discharge':
                cap.append(datas[i][j]['Capacity'][0][0][0])
                amb_temp.append(ambient_temperatures[i][j])

        Cycles[bs[i]]['Capacity'] = np.array(cap)
        Cycles[bs[i]]['ambient_temperatures'] = np.array(amb_temp)
    Cycles = pd.DataFrame(Cycles)

    return Cycles


def get_exp_based_df(exp):
    Cycles = preprocess_data_to_cycles()
    df_all = pd.DataFrame({})
    max_len = 0

    exp_try_out = exp

    for bat in exp_try_out:
        df = pd.DataFrame({})
        cols = ['Voltage_measured', 'Current_measured', 'Temperature_measured',
                'Current_load', 'Voltage_load', 'Time', 'Capacity', 'ambient_temperatures']
        for col in cols:
            df[col] = Cycles[bat][col]
        max_l = np.max(df['Time'].apply(lambda x: len(x)).values)
        max_len = max(max_l, max_len)
        df_all = pd.concat([df_all, df], ignore_index=True)

    df = df_all.reset_index(drop=True)

    for i, j in enumerate(df['Capacity']):
        try:
            if len(j):
                df['Capacity'][i] = j[0]
            else:
                df['Capacity'][i] = 0
        except:
            pass

    # CRITICAL TIME POINTS FOR A CYCLE
    # We will only these critical points for furthur training

    # TEMPERATURE_MEASURED
    # => Time at highest temperature

    # VOLTAGE_MEASURED
    # => Time at lowest Voltage

    # VOLTAGE_LOAD
    # => First time it drops below 1 volt after 1500 time

    def getTemperatureMeasuredCritical(tm, time):
        high = 0
        critical = 0
        for i in range(len(tm)):
            if (tm[i] > high):
                high = tm[i]
                critical = time[i]
        return critical

    def getVoltageMeasuredCritical(vm, time):
        low = 1e9
        critical = 0
        for i in range(len(vm)):
            if (vm[i] < low):
                low = vm[i]
                critical = time[i]
        return critical

    def getVoltageLoadCritical(vl, time):
        for i in range(len(vl)):
            if (time[i] > 1500 and vl[i] < 1):
                return time[i]
        return -1

    def fun(x):
        cap = x['Capacity']
        amb_temp = x['ambient_temperatures']
        volt_load_c = getVoltageLoadCritical(x['Voltage_load'], x['Time'])
        volt_meas_c = getVoltageMeasuredCritical(
            x['Voltage_measured'], x['Time'])
        temp_meas_c = getTemperatureMeasuredCritical(
            x['Temperature_measured'], x['Time'])

        data = {
            'Capacity': cap,
            'ambient_temperatures': amb_temp,
            'Critical_Voltage_load': volt_load_c,
            'Critical_Voltage_measured': volt_meas_c,
            'Critical_Temperature_measured': temp_meas_c,
        }
        data_idx = [
            'Capacity', 'ambient_temperatures', 'Critical_Voltage_load',
            'Critical_Voltage_measured', 'Critical_Temperature_measured',
        ]
        y = pd.Series(data, index=data_idx)

        return y

    df = df.apply(lambda x: fun(x), axis=1)

    df_x = df.drop(columns=['Capacity', 'ambient_temperatures']).values
    df_y = df['Capacity'].values

    return df_x, df_y
