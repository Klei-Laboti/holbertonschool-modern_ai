#!/usr/bin/env python3
"""Visualizes categorical feature distributions in a grid."""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Plot bar charts of value counts for each categorical column."""
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include="object").columns
        columns_to_plot = [c for c in columns_to_plot if c != "Churn"]
    else:
        columns_to_plot = columns_to_plot

    n_cols = 3
    n_rows = (len(columns_to_plot) + n_cols - 1) // n_cols
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))

    for i, col in enumerate(columns_to_plot):
        ax = axes[i // n_cols, i % n_cols]
        df[col].value_counts().plot(kind="bar", ax=ax)
        ax.set_title(col)
        ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
