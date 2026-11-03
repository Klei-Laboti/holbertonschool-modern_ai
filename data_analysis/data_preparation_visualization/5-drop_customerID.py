#!/usr/bin/env python3
"""Removes the customerID column from a DataFrame."""


def drop_customerID(df):
    """Drop the customerID column and return the modified DataFrame."""
    return df.drop(columns=["customerID"])
