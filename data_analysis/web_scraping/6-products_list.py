#!/usr/bin/env python3
"""Scrapes a static product category page using Selenium."""
import time
from selenium import webdriver


def scrape_products_list(url):
    """Open url in headless Chrome, return a list of product dicts."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    products = []
    try:
        driver.get(url)
        time.sleep(2)

        cards = driver.find_elements("css selector", "div.thumbnail")
        for card in cards:
            title = card.find_element(
                "css selector", "a.title").get_attribute("title")
            price = card.find_element("css selector", "h4.price").text
            description = card.find_element(
                "css selector", "p.description").text
            rating = len(card.find_elements(
                "css selector", "p.ratings > span.ws-icon-star"))
            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": rating,
            })
    finally:
        driver.quit()

    return products
