#!/usr/bin/env python3
"""Create a logistic regression classifier using Scikit-learn."""
from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """Create an untrained logistic regression classifier.

    Logistic regression performs binary classification by fitting a
    logistic function to the data and thresholding its output.

    Args:
        random_state: An integer used to set the random seed for
            reproducibility.

    Returns:
        model: An untrained LogisticRegression instance.
    """
    return linear_model.LogisticRegression(random_state=random_state)
