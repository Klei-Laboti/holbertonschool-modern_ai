#!/usr/bin/env python3
"""Removes duplicate rows from a DataFrame."""


def remove_duplicates(df):
    """Drop all duplicate rows and return the deduplicated DataFrame."""
    return df.drop_duplicates()
