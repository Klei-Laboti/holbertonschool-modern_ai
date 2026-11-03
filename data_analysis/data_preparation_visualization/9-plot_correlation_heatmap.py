#!/usr/bin/env python3
"""Visualizes correlations between continuous numeric features."""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """Plot an annotated correlation heatmap with the coolwarm colormap."""
    plt.figure(figsize=(6, 5))

    corr = df.select_dtypes(include="number").corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Correlation Matrix")
    plt.show()
