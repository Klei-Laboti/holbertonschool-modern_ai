#!/usr/bin/env python3
"""Create a lasso regression model using Scikit-learn."""
from sklearn import linear_model


def lasso_regression(random_state):
    """Create an untrained lasso regression model.

    Lasso regression extends ordinary least squares with an L1 penalty,
    which drives the coefficients of irrelevant features exactly to zero
    and therefore performs automatic feature selection.

    Args:
        random_state: An integer used to set the random seed for
            reproducibility.

    Returns:
        model: An untrained Lasso regression model instance.
    """
    return linear_model.Lasso(random_state=random_state)
