#!/usr/bin/env python3
"""Compares continuous numeric distributions by churn."""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """Plot overlapping histograms of a numeric column by Churn."""
    plt.figure(figsize=(12, 8))

    no = df[df["Churn"] == "No"][col]
    yes = df[df["Churn"] == "Yes"][col]

    plt.hist([no, yes], bins=30, label=["No", "Yes"])
    plt.title(col + " Distribution by Churn")
    plt.xlabel(col)
    plt.legend(title="Churn")
    plt.show()
