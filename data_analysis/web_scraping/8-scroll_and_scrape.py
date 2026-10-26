#!/usr/bin/env python3
"""Scrolls and scrapes all products from an infinite-scroll page."""
import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll to the bottom repeatedly, return unique product dicts."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    products = []
    seen = set()
    try:
        driver.get(url)
        time.sleep(scroll_pause)

        last_height = driver.execute_script(
            "return document.body.scrollHeight")
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause)
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        cards = driver.find_elements("css selector", "div.thumbnail")
        for card in cards:
            title = card.find_element(
                "css selector", "a.title").get_attribute("title")
            price = card.find_element("css selector", "h4.price").text
            description = card.find_element(
                "css selector", "p.description").text
            rating = len(card.find_elements(
                "css selector", "p.ratings > span.ws-icon-star"))

            key = (title, price)
            if key in seen:
                continue
            seen.add(key)
            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": rating,
            })
    finally:
        driver.quit()

    return products
