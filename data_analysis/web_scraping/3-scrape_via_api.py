#!/usr/bin/env python3
"""Scrapes quotes from the JSON API pages."""
import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Fetch all quotes from the JSON API, return list of quote dicts."""
    quotes = []
    page = 1

    while True:
        url = "{}/api/quotes?page={}".format(base_url, page)
        data = json.loads(fetch_html(url))

        for q in data["quotes"]:
            quotes.append({
                "text": q["text"],
                "author": q["author"]["name"],
                "tags": q["tags"],
            })

        if not data["has_next"]:
            break
        page += 1

    return quotes
