#!/usr/bin/env python3
"""Handles missing values in the TotalCharges column."""


def clean_total_charges(df, method='drop'):
    """Handle missing TotalCharges by drop, median or impute."""
    df = df.copy()
    if method == 'drop':
        df = df.dropna(subset=["TotalCharges"])
    elif method == 'median':
        median = df["TotalCharges"].median()
        df["TotalCharges"] = df["TotalCharges"].fillna(median)
    elif method == 'impute':
        imputed = df["MonthlyCharges"] * df["tenure"]
        df["TotalCharges"] = df["TotalCharges"].fillna(imputed)
    return df
