#!/usr/bin/env python3
"""Explain model predictions with the SHAP library."""
import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Build a SHAP explainer and compute SHAP values for a dataset.

    The training data is used as the background distribution the
    explainer compares each prediction against.

    Args:
        model: A trained regression model.
        X_train: Input data used to initialize the explainer.
        X_test: Input data to explain.

    Returns:
        tuple: (explainer, shap_values) where explainer is the SHAP
            explainer object and shap_values holds the SHAP values for
            the predictions on X_test.
    """
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
