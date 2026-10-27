#!/usr/bin/env python3
"""Scrape the products of a static category page with Selenium."""
import time
from selenium import webdriver

CSS = "css selector"


def make_driver():
    """Return a headless Chrome driver in a 1920x1080 window."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)


def scrape_products(url):
    """Return the products of a category page as a list of dicts.

    Each dict holds the title, price, description and star rating.
    Products that appear twice are kept only once.
    """
    driver = make_driver()
    try:
        driver.get(url)
        time.sleep(3)
        products = []
        seen = set()
        for card in driver.find_elements(CSS, ".thumbnail"):
            link = card.find_element(CSS, "a.title")
            price = card.find_element(CSS, "h4.price")
            desc = card.find_element(CSS, "p.description")
            stars = card.find_element(CSS, ".ratings p[data-rating]")
            product = {
                "title": link.get_attribute("title"),
                "price": price.text.strip(),
                "description": desc.text.strip(),
                "rating": int(stars.get_attribute("data-rating")),
            }
            key = (product["title"], product["price"],
                   product["description"])
            if key in seen:
                continue
            seen.add(key)
            products.append(product)
        return products
    finally:
        driver.quit()


scrape_products_list = scrape_products
