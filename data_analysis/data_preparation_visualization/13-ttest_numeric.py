#!/usr/bin/env python3
"""Performs Welch's t-tests for continuous numeric features."""
from scipy import stats


def ttest_numeric(df):
    """Return a dict of Welch t-test p-values per numeric feature."""
    results = {}
    numeric = df.select_dtypes(include="number").columns

    for col in numeric:
        yes = df[df["Churn"] == "Yes"][col].dropna()
        no = df[df["Churn"] == "No"][col].dropna()
        t_stat, p = stats.ttest_ind(yes, no, equal_var=False)
        results[col] = p

    return results
