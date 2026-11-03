#!/usr/bin/env python3
"""Visualizes missing values in a DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Scatter-plot missing values as vertical bars per column."""
    plt.figure(figsize=(12, 8))

    for i, col in enumerate(df.columns):
        missing = np.where(df[col].isnull())[0]
        plt.scatter(missing, np.full(len(missing), i), marker="|")

    plt.yticks(range(len(df.columns)), df.columns)
    plt.title("Missingness Plot")
    plt.tight_layout()
    plt.show()
