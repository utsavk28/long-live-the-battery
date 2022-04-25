import os
import pandas as pd

def preprocess() :
    path = "../input/rul-prediction-for-liion-batteries-prediction/Cleaned"
    path = "../../data/output/RNN/cleaned_results"
    exps_dict = {}
    exps = os.listdir(path)
    for exp in os.listdir(path):
        exps_dict[exp] = []
        for m in os.listdir(f"{path}/{exp}"):
            exps_dict[exp].append(m)

    pd.DataFrame(exps_dict)


    ensemble_dict = {}
    for exp in exps:
        df = pd.DataFrame()
        for m in exps_dict[exp]:
            model_name = m.split('_')[0]
            temp = pd.read_csv(f"{path}/{exp}/{m}").rename(
                columns={"Capacity": f"{model_name}_Cap", "model_predict": f"{model_name}_pred"})
            curr_cols = temp.columns.tolist()
            temp = temp.rename(columns={x: x.lower() for x in curr_cols})
            df = pd.concat([df, temp], axis=1)
        ensemble_dict[exp] = df

    ensemble_df = {}
    for exp in exps:
        print(exp)
        print(ensemble_dict[exp].columns.tolist())
        temp = ensemble_dict[exp].drop(
            columns=['gru_cap', 'bigru_cap', 'bilstm_cap']).rename(columns={'lstm_cap': 'cap'})
        df_x = temp.drop(columns=['cap'])
        df_y = temp['cap']
        ensemble_df[exp] = [df_x, df_y]
    
    return exps,exps_dict,ensemble_dict,ensemble_df