#!/usr/bin/env python3
"""Scroll an infinite-scroll page and scrape every product on it."""
import time
from selenium import webdriver

CSS = "css selector"
HEIGHT = "return document.body.scrollHeight"
BOTTOM = "window.scrollTo(0, document.body.scrollHeight);"
READ = (
    "return arguments[0].map(function (c) {"
    " return [c.querySelector('a.title').getAttribute('title'),"
    " c.querySelector('h4.price').textContent.trim(),"
    " c.querySelector('p.description').textContent.trim(),"
    " c.querySelectorAll('.ratings .ws-icon-star').length];"
    " });"
)


def make_driver():
    """Return a fast headless Chrome driver in a 1920x1080 window.

    Images are turned off and pages count as loaded once their HTML is
    ready, so the scrolling does not wait for pictures.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.page_load_strategy = "eager"
    return webdriver.Chrome(options=options)


def scroll_to_end(driver, scroll_pause):
    """Scroll to the bottom until the page height stops growing.

    After each scroll, waits up to scroll_pause seconds for the page to
    grow and moves on as soon as it does.
    """
    last_height = driver.execute_script(HEIGHT)
    while True:
        driver.execute_script(BOTTOM)
        new_height = last_height
        deadline = time.time() + scroll_pause
        while time.time() < deadline:
            time.sleep(0.1)
            new_height = driver.execute_script(HEIGHT)
            if new_height > last_height:
                break
        if new_height == last_height:
            break
        last_height = new_height


def scroll_and_scrape(url, scroll_pause=2.0):
    """Return every unique product of an infinite-scroll page.

    Scrolls until no new products load, finds every product card and
    reads its title, price, description and star count in one call.
    A product is skipped when its (title, price) pair was already seen.
    """
    driver = make_driver()
    try:
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element(CSS, "div.thumbnail")
        driver.implicitly_wait(0)
        scroll_to_end(driver, scroll_pause)
        cards = driver.find_elements(CSS, "div.thumbnail")
        products = []
        seen = set()
        for title, price, desc, stars in driver.execute_script(READ, cards):
            if (title, price) in seen:
                continue
            seen.add((title, price))
            products.append({
                "title": title,
                "price": price,
                "description": desc,
                "rating": stars,
            })
        return products
    finally:
        driver.quit()
