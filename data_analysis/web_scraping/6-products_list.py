#!/usr/bin/env python3
"""Scrapes a static product category page using Selenium."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


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

        cards = driver.find_elements(By.CLASS_NAME, "thumbnail")
        for card in cards:
            title = card.find_element(
                By.CSS_SELECTOR, "a.title").get_attribute("title")
            price = card.find_element(
                By.CSS_SELECTOR, "h4.price").text
            description = card.find_element(
                By.CSS_SELECTOR, "p.description").text
            rating = len(card.find_elements(
                By.CSS_SELECTOR, "p[data-rating] span.ws-icon-star"))
            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": rating,
            })
    finally:
        driver.quit()

    return products
