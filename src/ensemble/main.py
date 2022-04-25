import pandas as pd
from preprocess import preprocess
from utils import *

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.svm import LinearSVR, NuSVR, SVR
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.neighbors import KNeighborsRegressor

from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor


if __name__ == "__main__":
    exps, exps_dict, ensemble_dict, ensemble_df = preprocess()
    model_results = pd.DataFrame()
    for exp in exps:
        print(exp)
        df_x, df_y = ensemble_df[exp]
        train_x, test_x, train_y, test_y = train_test_split(
            df_x, df_y, test_size=0.2, random_state=0)
        test_x, val_x, test_y, val_y = train_test_split(
            test_x, test_y, test_size=0.5, random_state=0)

        print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)

        algos = (LinearRegression, HuberRegressor, KNeighborsRegressor, LinearSVR, NuSVR,
                 SVR, DecisionTreeRegressor, ExtraTreeRegressor, RandomForestRegressor, ExtraTreesRegressor,
                 XGBRegressor, LGBMRegressor, CatBoostRegressor)

        params = {
            'silent': True
        }

        for algo in algos:
            model = algo()
            if type(model).__name__ == 'CatBoostRegressor':
                model = algo(**params)
    #         print(type(model).__name__)
            model.fit(train_x, train_y)

            model_results_train = get_scores(
                train_y, get_preds(model, train_x))
            model_results_val = get_scores(val_y, get_preds(model, val_x))
            model_results_test = get_scores(test_y, get_preds(model, test_x))
            data = {"Train": model_results_train,
                    "Val": model_results_val,
                    "Test": model_results_test}
            temp = pd.DataFrame(data, index=[f'{exp}_{type(model).__name__}'])
            model_results = model_results.append(temp)

    model_results.to_csv('../../data/output/Ensemble/ensemble_results.csv')
