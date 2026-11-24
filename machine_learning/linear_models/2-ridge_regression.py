#!/usr/bin/env python3
"""Create a ridge regression model using Scikit-learn."""
from sklearn import linear_model


def ridge_regression(random_state):
    """Create an untrained ridge regression model.

    Ridge regression extends ordinary least squares with an L2 penalty,
    which shrinks large coefficients and stabilises the fit when the
    input features are correlated.

    Args:
        random_state: An integer used to set the random seed for
            reproducibility.

    Returns:
        model: An untrained Ridge regression model instance.
    """
    return linear_model.Ridge(random_state=random_state)
