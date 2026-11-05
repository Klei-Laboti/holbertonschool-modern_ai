#!/usr/bin/env python3
"""Visualizes the distributions of continuous numerical features."""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """Plot a histogram with KDE and a boxplot for each numeric column."""
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include="number").columns

    n_cols = len(columns_to_plot)
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3 * n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, col in enumerate(columns_to_plot):
        data = df[col].dropna()

        axes[i, 0].hist(data, bins=30, density=True, alpha=0.7,
                        edgecolor="black")
        kde = stats.gaussian_kde(data)
        x = np.linspace(data.min(), data.max(), 200)
        axes[i, 0].plot(x, kde(x), color="red", linestyle="--")
        axes[i, 0].set_title(col + " Histogram + KDE")

        axes[i, 1].boxplot(data, vert=False)
        axes[i, 1].set_title(col + " Boxplot")

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
