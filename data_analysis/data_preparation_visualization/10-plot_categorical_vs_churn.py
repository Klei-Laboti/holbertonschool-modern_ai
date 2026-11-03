#!/usr/bin/env python3
"""Visualizes churn rates per category for a categorical column."""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """Plot the churn rate (Yes proportion) per category as a bar plot."""
    plt.figure(figsize=(12, 8))

    churn_rate = df.groupby(col)["Churn"].apply(
        lambda x: (x == "Yes").mean())

    churn_rate.plot(kind="bar")
    plt.title("Churn Rate by " + col)
    plt.ylabel("Churn Rate")
    plt.xlabel("")
    plt.xticks(rotation=45)
    plt.show()
