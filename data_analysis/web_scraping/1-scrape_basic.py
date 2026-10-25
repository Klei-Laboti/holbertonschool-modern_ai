#!/usr/bin/env python3
"""Scrapes the first page of quotes using BeautifulSoup."""
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Return a list of quote dicts (text, author, tags) from url."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    quotes = []

    for block in soup.find_all("div", class_="quote"):
        text = block.find("span", class_="text").get_text()
        author = block.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in block.find_all("a", class_="tag")]
        quotes.append({"text": text, "author": author, "tags": tags})

    return quotes
