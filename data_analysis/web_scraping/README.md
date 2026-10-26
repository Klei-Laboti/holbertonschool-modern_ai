# Data Collection - Web Scraping

Scripts that fetch and scrape data from web pages using `requests`,
BeautifulSoup and Selenium: HTTP requests, pagination, JSON APIs,
JSON-LD extraction, authenticated scraping and headless browsing.

## Requirements
- Ubuntu 20.04 LTS, Python 3.9
- `requests`, `beautifulsoup4`, `selenium`
- pycodestyle 2.11.1
- All files start with `#!/usr/bin/env python3` and are executable

## Tasks
| File | Description |
|------|-------------|
| `0-fetch_html.py` | `fetch_html(url, headers={}, timeout=10)` - fetch a page, raise on status >= 400 |
| `1-scrape_basic.py` | `scrape_basic(url)` - scrape the first page of quotes with BeautifulSoup |
| `2-scrape_paginated.py` | `scrape_paginated(base_url)` - follow Next links across all pages |
| `3-scrape_via_api.py` | `scrape_via_api(base_url)` - scrape quotes from the JSON API |
| `4-extract_jsonld.py` | `extract_jsonld(url)` - extract quotes from embedded JSON-LD |
| `5-login_and_scrape.py` | `login_and_scrape(login_url, user, pwd)` - log in and scrape protected quotes |
| `6-products_list.py` | `scrape_products_list(url)` - scrape a product list with Selenium |
| `7-product_detail.py` | `scrape_product_detail(url, delay=2.0)` - scrape a single product detail page |
| `8-scroll_and_scrape.py` | `scroll_and_scrape(url, scroll_pause=2.0)` - scrape an infinite-scroll page |

## Author
Kleant Laboti
