#!/usr/bin/env python3
"""Extracts quotes from embedded JSON-LD on a page."""
import json
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Parse JSON-LD Quote objects from url, return list of quote dicts."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    quotes = []

    for script in soup.find_all("script", type="application/ld+json"):
        obj = json.loads(script.string)
        if obj.get("@type") != "Quote":
            continue
        text = obj.get("text")
        author = obj.get("author", {}).get("name")
        keywords = obj.get("keywords", [])
        if isinstance(keywords, str):
            tags = keywords.split(",")
        else:
            tags = keywords
        quotes.append({"text": text, "author": author, "tags": tags})

    return quotes
