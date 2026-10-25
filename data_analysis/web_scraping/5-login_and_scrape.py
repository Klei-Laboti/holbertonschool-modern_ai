#!/usr/bin/env python3
"""Logs in and scrapes quotes visible only after authentication."""
import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in with CSRF token, then scrape quotes, return quote dicts."""
    session = requests.Session()

    page = session.get(login_url)
    soup = BeautifulSoup(page.text, "html.parser")
    token = soup.find("input", {"name": "csrf_token"})["value"]

    payload = {"username": user, "password": pwd, "csrf_token": token}
    session.post(login_url, data=payload)

    base = login_url.replace("/login", "/")
    protected = session.get(base)
    soup = BeautifulSoup(protected.text, "html.parser")
    quotes = []

    for block in soup.find_all("div", class_="quote"):
        text = block.find("span", class_="text").get_text()
        author = block.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in block.find_all("a", class_="tag")]
        quotes.append({"text": text, "author": author, "tags": tags})

    return quotes
