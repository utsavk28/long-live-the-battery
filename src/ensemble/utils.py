import numpy as np
from sklearn.metrics import mean_squared_error


def get_scores(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))


def get_preds(model, data_x):
    return model.predict(data_x).clip(min=0)
