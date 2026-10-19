#!/usr/bin/env python3
"""Fetches a web page and returns its HTML as text."""
import requests


def fetch_html(url, headers={}, timeout=10):
    """Fetch url and return its full HTML; raise on status >= 400."""
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text
