#!/usr/bin/env python3
"""Visualizes missing values in a DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Scatter-plot missing values as vertical bars per column."""
    plt.figure(figsize=(12, 8))

    for i, col in enumerate(df.columns):
        missing = df.index[df[col].isnull()]
        plt.scatter(missing, [i] * len(missing), marker="|")

    plt.yticks(range(len(df.columns)), df.columns)
    plt.tight_layout()
    plt.show()
