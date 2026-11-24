#!/usr/bin/env python3
"""Create a linear regression model using Scikit-learn."""
from sklearn import linear_model


def Linear_Regression():
    """Create an untrained ordinary least squares linear model.

    Returns:
        model: An untrained LinearRegression instance.
    """
    return linear_model.LinearRegression()
