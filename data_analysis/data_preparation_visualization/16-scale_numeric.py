#!/usr/bin/env python3
"""Standardizes numeric columns using StandardScaler."""
from sklearn import preprocessing


def scale_numeric(df):
    """Scale MonthlyCharges and TotalCharges to mean 0, std 1."""
    df = df.copy()
    cols = ["MonthlyCharges", "TotalCharges"]
    scaler = preprocessing.StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df
