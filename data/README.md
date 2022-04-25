# Data
## Dataset
## Dataset Overview
The dataset has been collected from a custom-built battery prognostics tested at the NASA Ames Prognostics Center of Excellence. The Lithium-ion batteries were run through 2 different operational profiles (charging and discharging) at different temperatures. The experiments were stopped when the batteries reached the end-of-life (EOL) criteria of 30% fade in rated capacity (from 2 Ah to 1.4 Ah)
### Dataset Structure
##### Charge
1. Voltage_measured: Battery terminal voltage (Volts)
2. Current_measured: Battery output current (Amps)
3. Temperature_measured: Battery temperature (degree C)
4. Current_charge: Current measured at charger (Amps)
5. Voltage_charge: Voltage measured at charger (Volts)
6. Time: Time vector for the cycle (secs)

##### Discharge
1. Voltage_measured: Battery terminal voltage (Volts)
2. Current_measured: Battery output current (Amps)
3. Temperature_measured: Battery temperature (degree C)
4. Current_charge: Current measured at load (Amps)
5. Voltage_charge: Voltage measured at load (Volts)
6. Time: Time vector for the cycle (secs)
7. Capacity: Battery capacity (Ahr) for discharge till 2.7V

##### Impedance
1. Sense_current: Current in sense branch (Amps)
2. Battery_current: Current in battery branch (Amps)
3. Current_ratio: Ratio of the above currents
4. Battery_impedance: Battery impedance (Ohms) computed from raw data
5. Rectified_impedance: Calibrated and smoothed battery impedance (Ohms)
6. Re: Estimated electrolyte resistance (Ohms)
7. Rct: Estimated charge transfer resistance (Ohms)


## Folder Structure & Files
```
📁 data/
├─📁 input/
│ └─📁 battery-data-set/
│   ├─📁 BatteryAgingARC-FY08Q4/
│   │ ├─📄 B0005.mat
│   │ ├─📄 B0006.mat
│   │ ├─📄 B0007.mat
│   │ ├─📄 B0018.mat
│   │ └─📄 README.txt
│   ├─📁 BatteryAgingARC_25-44/
│   │ ├─📄 B0025.mat
│   │ ├─📄 B0026.mat
│   │ ├─📄 B0027.mat
│   │ ├─📄 B0028.mat
│   │ ├─📄 B0029.mat
│   │ ├─📄 B0030.mat
│   │ ├─📄 B0031.mat
│   │ ├─📄 B0032.mat
│   │ ├─📄 B0033.mat
│   │ ├─📄 B0034.mat
│   │ ├─📄 B0036.mat
│   │ ├─📄 B0038.mat
│   │ ├─📄 B0039.mat
│   │ ├─📄 B0040.mat
│   │ ├─📄 B0041.mat
│   │ ├─📄 B0042.mat
│   │ ├─📄 B0043.mat
│   │ ├─📄 B0044.mat
│   │ ├─📄 README_25_26_27_28.txt
│   │ ├─📄 README_29_30_31_32.txt
│   │ ├─📄 README_33_34_36.txt
│   │ ├─📄 README_38_39_40.txt
│   │ └─📄 README_41_42_43_44.txt
│   ├─📁 BatteryAgingARC_25_26_27_28_P1/
│   │ ├─📄 B0025.mat
│   │ ├─📄 B0026.mat
│   │ ├─📄 B0027.mat
│   │ ├─📄 B0028.mat
│   │ └─📄 README.txt
│   ├─📁 BatteryAgingARC_45_46_47_48/
│   │ ├─📄 B0045.mat
│   │ ├─📄 B0046.mat
│   │ ├─📄 B0047.mat
│   │ ├─📄 B0048.mat
│   │ └─📄 README_45_46_47_48.txt
│   ├─📁 BatteryAgingARC_49_50_51_52/
│   │ ├─📄 B0049.mat
│   │ ├─📄 B0050.mat
│   │ ├─📄 B0051.mat
│   │ ├─📄 B0052.mat
│   │ └─📄 README_49_50_51_52.txt
│   └─📁 BatteryAgingARC_53_54_55_56/
│     ├─📄 B0053.mat
│     ├─📄 B0054.mat
│     ├─📄 B0055.mat
│     ├─📄 B0056.mat
│     └─📄 README_53_54_55_56.txt
├─📁 output/
│ ├─📁 Critical_Point/
│ │ └─📄 critical_point_results.csv
│ ├─📁 Ensemble/
│ │ └─📄 ensemble_results.csv
│ └─📁 RNN/
│   ├─📁 cleaned_results/
│   │ ├─📁 Experiment 1/
│   │ │ ├─📄 BIGRU_EXP_1.csv
│   │ │ ├─📄 BILSTM_EXP_1.csv
│   │ │ ├─📄 GRU_EXP_1.csv
│   │ │ └─📄 LSTM_EXP_1.csv
│   │ ├─📁 Experiment 2/
│   │ │ ├─📄 bigru_exp_2_results.csv
│   │ │ ├─📄 bilstm_exp_2_results.csv
│   │ │ ├─📄 gru_exp_2_results.csv
│   │ │ └─📄 lstm_exp_2_results.csv
│   │ ├─📁 Experiment 3/
│   │ │ ├─📄 bigur_exp_3_results.csv
│   │ │ ├─📄 bilstm_exp_3_results.csv
│   │ │ ├─📄 gru_exp_3_results.csv
│   │ │ └─📄 lstm_exp_3_results.csv
│   │ ├─📁 Experiment 4/
│   │ │ ├─📄 33_34_36_BiGRU_results.csv
│   │ │ ├─📄 33_34_36_BiLSTM_results.csv
│   │ │ ├─📄 33_34_36_GRU_results.csv
│   │ │ └─📄 33_34_36_LSTM_results.csv
│   │ ├─📁 Experiment 5/
│   │ │ ├─📄 38_39_40_BiGRU_results.csv
│   │ │ ├─📄 38_39_40_BiLSTM_results.csv
│   │ │ ├─📄 38_39_40_GRU_results.csv
│   │ │ └─📄 38_39_40_LSTM_results.csv
│   │ ├─📁 Experiment 6/
│   │ │ ├─📄 41_42_43_44_BiGRU_results.csv
│   │ │ ├─📄 41_42_43_44_BiLSTM_results.csv
│   │ │ ├─📄 41_42_43_44_GRU_results.csv
│   │ │ └─📄 41_42_43_44_LSTM_results.csv
│   │ ├─📁 Experiment 7/
│   │ │ ├─📄 7_BiGRU_results.csv
│   │ │ ├─📄 7_BiLSTM_results.csv
│   │ │ ├─📄 7_GRU_results.csv
│   │ │ └─📄 7_LSTM_results.csv
│   │ ├─📁 Experiment 8/
│   │ │ ├─📄 8_BiGRU_results.csv
│   │ │ ├─📄 8_BiLSTM_results.csv
│   │ │ ├─📄 8_GRU_results.csv
│   │ │ └─📄 8_LSTM_results.csv
│   │ └─📁 Experiment 9/
│   │   ├─📄 9_BiGRU_results.csv
│   │   ├─📄 9_BiLSTM_results.csv
│   │   ├─📄 9_GRU_results.csv
│   │   └─📄 9_LSTM_results.csv
│   ├─📁 models/
│   │ ├─📁 Exp4/
│   │ │ ├─📄 33_34_36_BiGRU.csv
│   │ │ ├─📄 33_34_36_BiGRU.h5
│   │ │ ├─📄 33_34_36_BiLSTM.csv
│   │ │ ├─📄 33_34_36_BiLSTM.h5
│   │ │ ├─📄 33_34_36_GRU.csv
│   │ │ ├─📄 33_34_36_GRU.h5
│   │ │ ├─📄 33_34_36_LSTM.csv
│   │ │ └─📄 33_34_36_LSTM.h5
│   │ ├─📁 Exp5/
│   │ │ ├─📄 38_39_40_BiGRU.csv
│   │ │ ├─📄 38_39_40_BiGRU.h5
│   │ │ ├─📄 38_39_40_BiLSTM.csv
│   │ │ ├─📄 38_39_40_BiLSTM.h5
│   │ │ ├─📄 38_39_40_GRU.csv
│   │ │ ├─📄 38_39_40_GRU.h5
│   │ │ ├─📄 38_39_40_LSTM.csv
│   │ │ └─📄 38_39_40_LSTM.h5
│   │ ├─📁 Exp6/
│   │ │ ├─📄 41_42_43_44_BiGRU.csv
│   │ │ ├─📄 41_42_43_44_BiGRU.h5
│   │ │ ├─📄 41_42_43_44_BiLSTM.csv
│   │ │ ├─📄 41_42_43_44_BiLSTM.h5
│   │ │ ├─📄 41_42_43_44_GRU.csv
│   │ │ ├─📄 41_42_43_44_GRU.h5
│   │ │ ├─📄 41_42_43_44_LSTM.csv
│   │ │ └─📄 41_42_43_44_LSTM.h5
│   │ ├─📁 Experiment 1/
│   │ │ ├─📄 bigru_exp_1.csv
│   │ │ ├─📄 bigru_exp_1.h5
│   │ │ ├─📄 bilstm_exp_1.csv
│   │ │ ├─📄 bilstm_exp_1.h5
│   │ │ ├─📄 gru_exp_1.csv
│   │ │ ├─📄 gru_exp_1.h5
│   │ │ ├─📄 lstm_exp_1.csv
│   │ │ └─📄 lstm_exp_1.h5
│   │ ├─📁 Experiment 2/
│   │ │ ├─📄 bigru_exp_2.csv
│   │ │ ├─📄 bigru_exp_2.h5
│   │ │ ├─📄 bilstm_exp_2.csv
│   │ │ ├─📄 bilstm_exp_2.h5
│   │ │ ├─📄 gru_exp_2.csv
│   │ │ ├─📄 gru_exp_2.h5
│   │ │ ├─📄 lstm_exp_2.csv
│   │ │ └─📄 lstm_exp_2.h5
│   │ ├─📁 Experiment 3/
│   │ │ ├─📄 bigru_exp_3.csv
│   │ │ ├─📄 bigur_exp_3.h5
│   │ │ ├─📄 bilstm_exp_3.csv
│   │ │ ├─📄 bilstm_exp_3.h5
│   │ │ ├─📄 gru_exp_3.csv
│   │ │ ├─📄 gru_exp_3.h5
│   │ │ ├─📄 lstm_exp_3.csv
│   │ │ └─📄 lstm_exp_3.h5
│   │ ├─📁 Experiment 7/
│   │ │ ├─📄 7_BiGRU.csv
│   │ │ ├─📄 7_BiGRU.h5
│   │ │ ├─📄 7_BiLSTM.csv
│   │ │ ├─📄 7_BiLSTM.h5
│   │ │ ├─📄 7_GRU.csv
│   │ │ ├─📄 7_GRU.h5
│   │ │ ├─📄 7_LSTM.csv
│   │ │ └─📄 7_LSTM.h5
│   │ ├─📁 Experiment8/
│   │ │ ├─📄 8_BiGRU.csv
│   │ │ ├─📄 8_BiGRU.h5
│   │ │ ├─📄 8_BiLSTM.csv
│   │ │ ├─📄 8_BiLSTM.h5
│   │ │ ├─📄 8_GRU.csv
│   │ │ ├─📄 8_GRU.h5
│   │ │ ├─📄 8_LSTM.csv
│   │ │ └─📄 8_LSTM.h5
│   │ └─📁 Experiment9/
│   │   ├─📄 9_BiGRU.csv
│   │   ├─📄 9_BiGRU.h5
│   │   ├─📄 9_BiLSTM.csv
│   │   ├─📄 9_BiLSTM.h5
│   │   ├─📄 9_GRU.csv
│   │   ├─📄 9_GRU.h5
│   │   ├─📄 9_LSTM.csv
│   │   └─📄 9_LSTM.h5
│   └─📁 results/
│     ├─📁 Experiment 1/
│     │ ├─📄 BIGRU_EXP_1.csv
│     │ ├─📄 BILSTM_EXP_1.csv
│     │ ├─📄 GRU_EXP_1.csv
│     │ └─📄 LSTM_EXP_1.csv
│     ├─📁 Experiment 2/
│     │ ├─📄 bigru_exp_2_results.csv
│     │ ├─📄 bilstm_exp_2_results.csv
│     │ ├─📄 gru_exp_2_results.csv
│     │ └─📄 lstm_exp_2_results.csv
│     ├─📁 Experiment 3/
│     │ ├─📄 bigur_exp_3_results.csv
│     │ ├─📄 bilstm_exp_3_results.csv
│     │ ├─📄 gru_exp_3_results.csv
│     │ └─📄 lstm_exp_3_results.csv
│     ├─📁 Experiment 4/
│     │ ├─📄 33_34_36_BiGRU_results.csv
│     │ ├─📄 33_34_36_BiLSTM_results.csv
│     │ ├─📄 33_34_36_GRU_results.csv
│     │ └─📄 33_34_36_LSTM_results.csv
│     ├─📁 Experiment 5/
│     │ ├─📄 38_39_40_BiGRU_results.csv
│     │ ├─📄 38_39_40_BiLSTM_results.csv
│     │ ├─📄 38_39_40_GRU_results.csv
│     │ └─📄 38_39_40_LSTM_results.csv
│     ├─📁 Experiment 6/
│     │ ├─📄 41_42_43_44_BiGRU_results.csv
│     │ ├─📄 41_42_43_44_BiLSTM_results.csv
│     │ ├─📄 41_42_43_44_GRU_results.csv
│     │ └─📄 41_42_43_44_LSTM_results.csv
│     ├─📁 Experiment 7/
│     │ ├─📄 7_BiGRU_results.csv
│     │ ├─📄 7_GRU_results.csv
│     │ └─📄 7_LSTM_results.csv
│     ├─📁 Experiment 8/
│     │ ├─📄 8_BiGRU_results.csv
│     │ ├─📄 8_BiLSTM_results.csv
│     │ ├─📄 8_GRU_results.csv
│     │ └─📄 8_LSTM_results.csv
│     └─📁 Experiment 9/
│       ├─📄 9_BiGRU_results.csv
│       ├─📄 9_BiLSTM_results.csv
│       ├─📄 9_GRU_results.csv
│       └─📄 9_LSTM_results.csv
└─📄 README.md
>>> sd.seedir('./data', style='emoji', indent=4)
📁 data/
├───📁 input/
│   └───📁 battery-data-set/
│       ├───📁 BatteryAgingARC-FY08Q4/
│       │   ├───📄 B0005.mat
│       │   ├───📄 B0006.mat
│       │   ├───📄 B0007.mat
│       │   ├───📄 B0018.mat
│       │   └───📄 README.txt
│       ├───📁 BatteryAgingARC_25-44/
│       │   ├───📄 B0025.mat
│       │   ├───📄 B0026.mat
│       │   ├───📄 B0027.mat
│       │   ├───📄 B0028.mat
│       │   ├───📄 B0029.mat
│       │   ├───📄 B0030.mat
│       │   ├───📄 B0031.mat
│       │   ├───📄 B0032.mat
│       │   ├───📄 B0033.mat
│       │   ├───📄 B0034.mat
│       │   ├───📄 B0036.mat
│       │   ├───📄 B0038.mat
│       │   ├───📄 B0039.mat
│       │   ├───📄 B0040.mat
│       │   ├───📄 B0041.mat
│       │   ├───📄 B0042.mat
│       │   ├───📄 B0043.mat
│       │   ├───📄 B0044.mat
│       │   ├───📄 README_25_26_27_28.txt
│       │   ├───📄 README_29_30_31_32.txt
│       │   ├───📄 README_33_34_36.txt
│       │   ├───📄 README_38_39_40.txt
│       │   └───📄 README_41_42_43_44.txt
│       ├───📁 BatteryAgingARC_25_26_27_28_P1/
│       │   ├───📄 B0025.mat
│       │   ├───📄 B0026.mat
│       │   ├───📄 B0027.mat
│       │   ├───📄 B0028.mat
│       │   └───📄 README.txt
│       ├───📁 BatteryAgingARC_45_46_47_48/
│       │   ├───📄 B0045.mat
│       │   ├───📄 B0046.mat
│       │   ├───📄 B0047.mat
│       │   ├───📄 B0048.mat
│       │   └───📄 README_45_46_47_48.txt
│       ├───📁 BatteryAgingARC_49_50_51_52/
│       │   ├───📄 B0049.mat
│       │   ├───📄 B0050.mat
│       │   ├───📄 B0051.mat
│       │   ├───📄 B0052.mat
│       │   └───📄 README_49_50_51_52.txt
│       └───📁 BatteryAgingARC_53_54_55_56/
│           ├───📄 B0053.mat
│           ├───📄 B0054.mat
│           ├───📄 B0055.mat
│           ├───📄 B0056.mat
│           └───📄 README_53_54_55_56.txt
├───📁 output/
│   ├───📁 Critical_Point/
│   │   └───📄 critical_point_results.csv
│   ├───📁 Ensemble/
│   │   └───📄 ensemble_results.csv
│   └───📁 RNN/
│       ├───📁 cleaned_results/
│       │   ├───📁 Experiment 1/
│       │   │   ├───📄 BIGRU_EXP_1.csv
│       │   │   ├───📄 BILSTM_EXP_1.csv
│       │   │   ├───📄 GRU_EXP_1.csv
│       │   │   └───📄 LSTM_EXP_1.csv
│       │   ├───📁 Experiment 2/
│       │   │   ├───📄 bigru_exp_2_results.csv
│       │   │   ├───📄 bilstm_exp_2_results.csv
│       │   │   ├───📄 gru_exp_2_results.csv
│       │   │   └───📄 lstm_exp_2_results.csv
│       │   ├───📁 Experiment 3/
│       │   │   ├───📄 bigur_exp_3_results.csv
│       │   │   ├───📄 bilstm_exp_3_results.csv
│       │   │   ├───📄 gru_exp_3_results.csv
│       │   │   └───📄 lstm_exp_3_results.csv
│       │   ├───📁 Experiment 4/
│       │   │   ├───📄 33_34_36_BiGRU_results.csv
│       │   │   ├───📄 33_34_36_BiLSTM_results.csv
│       │   │   ├───📄 33_34_36_GRU_results.csv
│       │   │   └───📄 33_34_36_LSTM_results.csv
│       │   ├───📁 Experiment 5/
│       │   │   ├───📄 38_39_40_BiGRU_results.csv
│       │   │   ├───📄 38_39_40_BiLSTM_results.csv
│       │   │   ├───📄 38_39_40_GRU_results.csv
│       │   │   └───📄 38_39_40_LSTM_results.csv
│       │   ├───📁 Experiment 6/
│       │   │   ├───📄 41_42_43_44_BiGRU_results.csv
│       │   │   ├───📄 41_42_43_44_BiLSTM_results.csv
│       │   │   ├───📄 41_42_43_44_GRU_results.csv
│       │   │   └───📄 41_42_43_44_LSTM_results.csv
│       │   ├───📁 Experiment 7/
│       │   │   ├───📄 7_BiGRU_results.csv
│       │   │   ├───📄 7_BiLSTM_results.csv
│       │   │   ├───📄 7_GRU_results.csv
│       │   │   └───📄 7_LSTM_results.csv
│       │   ├───📁 Experiment 8/
│       │   │   ├───📄 8_BiGRU_results.csv
│       │   │   ├───📄 8_BiLSTM_results.csv
│       │   │   ├───📄 8_GRU_results.csv
│       │   │   └───📄 8_LSTM_results.csv
│       │   └───📁 Experiment 9/
│       │       ├───📄 9_BiGRU_results.csv
│       │       ├───📄 9_BiLSTM_results.csv
│       │       ├───📄 9_GRU_results.csv
│       │       └───📄 9_LSTM_results.csv
│       ├───📁 models/
│       │   ├───📁 Exp4/
│       │   │   ├───📄 33_34_36_BiGRU.csv
│       │   │   ├───📄 33_34_36_BiGRU.h5
│       │   │   ├───📄 33_34_36_BiLSTM.csv
│       │   │   ├───📄 33_34_36_BiLSTM.h5
│       │   │   ├───📄 33_34_36_GRU.csv
│       │   │   ├───📄 33_34_36_GRU.h5
│       │   │   ├───📄 33_34_36_LSTM.csv
│       │   │   └───📄 33_34_36_LSTM.h5
│       │   ├───📁 Exp5/
│       │   │   ├───📄 38_39_40_BiGRU.csv
│       │   │   ├───📄 38_39_40_BiGRU.h5
│       │   │   ├───📄 38_39_40_BiLSTM.csv
│       │   │   ├───📄 38_39_40_BiLSTM.h5
│       │   │   ├───📄 38_39_40_GRU.csv
│       │   │   ├───📄 38_39_40_GRU.h5
│       │   │   ├───📄 38_39_40_LSTM.csv
│       │   │   └───📄 38_39_40_LSTM.h5
│       │   ├───📁 Exp6/
│       │   │   ├───📄 41_42_43_44_BiGRU.csv
│       │   │   ├───📄 41_42_43_44_BiGRU.h5
│       │   │   ├───📄 41_42_43_44_BiLSTM.csv
│       │   │   ├───📄 41_42_43_44_BiLSTM.h5
│       │   │   ├───📄 41_42_43_44_GRU.csv
│       │   │   ├───📄 41_42_43_44_GRU.h5
│       │   │   ├───📄 41_42_43_44_LSTM.csv
│       │   │   └───📄 41_42_43_44_LSTM.h5
│       │   ├───📁 Experiment 1/
│       │   │   ├───📄 bigru_exp_1.csv
│       │   │   ├───📄 bigru_exp_1.h5
│       │   │   ├───📄 bilstm_exp_1.csv
│       │   │   ├───📄 bilstm_exp_1.h5
│       │   │   ├───📄 gru_exp_1.csv
│       │   │   ├───📄 gru_exp_1.h5
│       │   │   ├───📄 lstm_exp_1.csv
│       │   │   └───📄 lstm_exp_1.h5
│       │   ├───📁 Experiment 2/
│       │   │   ├───📄 bigru_exp_2.csv
│       │   │   ├───📄 bigru_exp_2.h5
│       │   │   ├───📄 bilstm_exp_2.csv
│       │   │   ├───📄 bilstm_exp_2.h5
│       │   │   ├───📄 gru_exp_2.csv
│       │   │   ├───📄 gru_exp_2.h5
│       │   │   ├───📄 lstm_exp_2.csv
│       │   │   └───📄 lstm_exp_2.h5
│       │   ├───📁 Experiment 3/
│       │   │   ├───📄 bigru_exp_3.csv
│       │   │   ├───📄 bigur_exp_3.h5
│       │   │   ├───📄 bilstm_exp_3.csv
│       │   │   ├───📄 bilstm_exp_3.h5
│       │   │   ├───📄 gru_exp_3.csv
│       │   │   ├───📄 gru_exp_3.h5
│       │   │   ├───📄 lstm_exp_3.csv
│       │   │   └───📄 lstm_exp_3.h5
│       │   ├───📁 Experiment 7/
│       │   │   ├───📄 7_BiGRU.csv
│       │   │   ├───📄 7_BiGRU.h5
│       │   │   ├───📄 7_BiLSTM.csv
│       │   │   ├───📄 7_BiLSTM.h5
│       │   │   ├───📄 7_GRU.csv
│       │   │   ├───📄 7_GRU.h5
│       │   │   ├───📄 7_LSTM.csv
│       │   │   └───📄 7_LSTM.h5
│       │   ├───📁 Experiment8/
│       │   │   ├───📄 8_BiGRU.csv
│       │   │   ├───📄 8_BiGRU.h5
│       │   │   ├───📄 8_BiLSTM.csv
│       │   │   ├───📄 8_BiLSTM.h5
│       │   │   ├───📄 8_GRU.csv
│       │   │   ├───📄 8_GRU.h5
│       │   │   ├───📄 8_LSTM.csv
│       │   │   └───📄 8_LSTM.h5
│       │   └───📁 Experiment9/
│       │       ├───📄 9_BiGRU.csv
│       │       ├───📄 9_BiLSTM.csv
│       │       ├───📄 9_BiLSTM.h5
│       │       ├───📄 9_GRU.csv
│       │       ├───📄 9_GRU.h5
│       │       ├───📄 9_LSTM.csv
│       │       └───📄 9_LSTM.h5
│       └───📁 results/
│           ├───📁 Experiment 1/
│           │   ├───📄 BIGRU_EXP_1.csv
│           │   ├───📄 BILSTM_EXP_1.csv
│           │   ├───📄 GRU_EXP_1.csv
│           │   └───📄 LSTM_EXP_1.csv
│           ├───📁 Experiment 2/
│           │   ├───📄 bigru_exp_2_results.csv
│           │   ├───📄 bilstm_exp_2_results.csv
│           │   ├───📄 gru_exp_2_results.csv
│           │   └───📄 lstm_exp_2_results.csv
│           ├───📁 Experiment 3/
│           │   ├───📄 bigur_exp_3_results.csv
│           │   ├───📄 bilstm_exp_3_results.csv
│           │   ├───📄 gru_exp_3_results.csv
│           │   └───📄 lstm_exp_3_results.csv
│           ├───📁 Experiment 4/
│           │   ├───📄 33_34_36_BiGRU_results.csv
│           │   ├───📄 33_34_36_BiLSTM_results.csv
│           │   ├───📄 33_34_36_GRU_results.csv
│           │   └───📄 33_34_36_LSTM_results.csv
│           ├───📁 Experiment 5/
│           │   ├───📄 38_39_40_BiGRU_results.csv
│           │   ├───📄 38_39_40_BiLSTM_results.csv
│           │   ├───📄 38_39_40_GRU_results.csv
│           │   └───📄 38_39_40_LSTM_results.csv
│           ├───📁 Experiment 6/
│           │   ├───📄 41_42_43_44_BiGRU_results.csv
│           │   ├───📄 41_42_43_44_BiLSTM_results.csv
│           │   ├───📄 41_42_43_44_GRU_results.csv
│           │   └───📄 41_42_43_44_LSTM_results.csv
│           ├───📁 Experiment 7/
│           │   ├───📄 7_BiGRU_results.csv
│           │   ├───📄 7_BiLSTM_results.csv
│           │   ├───📄 7_GRU_results.csv
│           │   └───📄 7_LSTM_results.csv
│           ├───📁 Experiment 8/
│           │   ├───📄 8_BiGRU_results.csv
│           │   ├───📄 8_BiLSTM_results.csv
│           │   ├───📄 8_GRU_results.csv
│           │   └───📄 8_LSTM_results.csv
│           └───📁 Experiment 9/
│               ├───📄 9_BiGRU_results.csv
│               ├───📄 9_BiLSTM_results.csv
│               ├───📄 9_GRU_results.csv
│               └───📄 9_LSTM_results.csv
└───📄 README.md
```
