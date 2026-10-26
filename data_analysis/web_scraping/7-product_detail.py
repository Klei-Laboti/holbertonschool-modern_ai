#!/usr/bin/env python3
"""Scrapes a single product detail page using Selenium."""
import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Open a product detail page and return its details as a dict."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(delay)

        caption = driver.find_element("css selector", ".caption")
        title = caption.find_elements("css selector", "h4")[1].text
        price = driver.find_element("css selector", "h4.price").text
        description = driver.find_element(
            "css selector", "p.description").text
        rating = len(driver.find_elements(
            "css selector", ".ratings p.ws-icon-star"))

        detail = {
            "title": title,
            "price": price,
            "description": description,
            "rating": rating,
        }
    finally:
        driver.quit()

    return detail
