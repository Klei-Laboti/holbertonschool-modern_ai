#!/usr/bin/env python3
"""Encodes features for modeling using Scikit-learn."""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encode categorical features and return the encoders used."""
    df = df.copy()

    churn_le = preprocessing.LabelEncoder()
    df["Churn"] = churn_le.fit_transform(df["Churn"])

    binary_cols = ["Partner", "Dependents", "PaperlessBilling",
                   "SeniorCitizen"]
    binary_oe = preprocessing.OrdinalEncoder(
        categories=[["No", "Yes"]] * len(binary_cols))
    df[binary_cols] = binary_oe.fit_transform(df[binary_cols]).astype(int)

    df = pd.get_dummies(df, columns=["Contract", "PaymentMethod"],
                        drop_first=True)

    tenure_oe = preprocessing.OrdinalEncoder()
    df["TenureGroup"] = tenure_oe.fit_transform(
        df[["TenureGroup"]]).astype(int)

    dummy_cols = df.select_dtypes(include="bool").columns
    df[dummy_cols] = df[dummy_cols].astype(int)

    return df, churn_le, binary_oe, tenure_oe
