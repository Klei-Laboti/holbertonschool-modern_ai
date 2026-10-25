#!/usr/bin/env python3
"""Scrapes all pages of quotes by following Next links."""
import time
from urllib import parse
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """Follow Next links from base_url and return all quote dicts."""
    quotes = []
    url = base_url

    while url is not None:
        quotes += scrape_basic(url)

        html = fetch_html(url)
        soup = BeautifulSoup(html, "html.parser")
        next_li = soup.find("li", class_="next")
        if next_li is not None:
            href = next_li.find("a")["href"]
            url = parse.urljoin(base_url, href)
            time.sleep(1)
        else:
            url = None

    return quotes
