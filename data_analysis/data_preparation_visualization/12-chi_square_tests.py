#!/usr/bin/env python3
"""Performs chi-square tests for categorical features against Churn."""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """Return a dict of chi-square p-values per categorical feature."""
    results = {}
    categorical = df.select_dtypes(include="object").columns

    for col in categorical:
        if col == "Churn":
            continue
        contingency = pd.crosstab(df[col], df["Churn"])
        chi2, p, dof, expected = stats.chi2_contingency(contingency)
        results[col] = p

    return results
