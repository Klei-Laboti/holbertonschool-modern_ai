#!/usr/bin/env python3
"""Engineers new features from the dataset."""
import pandas as pd


def create_features(df):
    """Create NumServices and TenureGroup, drop source columns."""
    df = df.copy()

    service_cols = [
        "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies",
        "MultipleLines",
    ]

    num_services = (df[service_cols] == "Yes").sum(axis=1)
    num_services += (df["InternetService"] != "No").astype(int)
    df["NumServices"] = num_services

    bins = [0, 12, 24, 48, 60, float("inf")]
    labels = ["0-12", "13-24", "25-48", "49-60", "60+"]
    df["TenureGroup"] = pd.cut(df["tenure"], bins=bins, labels=labels)

    df = df.drop(columns=service_cols + ["InternetService", "tenure"])

    return df
