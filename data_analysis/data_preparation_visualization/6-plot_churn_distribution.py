#!/usr/bin/env python3
"""Visualizes the churn class distribution as a bar plot."""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Plot a bar chart of Churn value counts (No skyblue, Yes salmon)."""
    churn_counts = df["Churn"].value_counts()

    plt.figure(figsize=(12, 8))
    churn_counts.plot(kind="bar", color=["skyblue", "salmon"])
    plt.title("Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.show()
