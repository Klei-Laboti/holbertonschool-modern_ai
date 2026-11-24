#!/usr/bin/env python3
"""Compute common evaluation metrics for regression tasks."""
from sklearn import metrics
import numpy as np


def evaluation_metrics_for_regression(y_true, y_pred):
    """Compute MSE, RMSE, MAE and R2 for a set of predictions.

    Args:
        y_true: A 1D NumPy array containing the true target values.
        y_pred: A 1D NumPy array containing the predicted target values.

    Returns:
        tuple: (mse, rmse, mae, r2) where mse is the mean squared error,
            rmse the root mean squared error, mae the mean absolute error
            and r2 the coefficient of determination.
    """
    mse = metrics.mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = metrics.mean_absolute_error(y_true, y_pred)
    r2 = metrics.r2_score(y_true, y_pred)
    return mse, rmse, mae, r2
