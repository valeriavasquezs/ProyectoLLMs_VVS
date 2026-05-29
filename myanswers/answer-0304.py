import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import LeaveOneOut, cross_val_score


def evaluar_robustez_loocv(X, y, modelo_tipo):
    if modelo_tipo == "linear":
        modelo = LinearRegression()
    elif modelo_tipo == "ridge":
        modelo = Ridge(alpha=1.0)
    else:
        raise ValueError("modelo_tipo debe ser 'linear' o 'ridge'")

    loo = LeaveOneOut()
    scores = cross_val_score(modelo, X, y, cv=loo, scoring="neg_mean_squared_error")

    return float(-scores.mean())
