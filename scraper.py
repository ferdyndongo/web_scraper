#!/usr/bin/env python3
from web_scraper import web_page_scraper

# url = input()
# get_content_type(address=url)
# get_movie_description(url)
url = 'https://www.nature.com/nature/articles'
# web_scraper(url)
n_pages = int(input())
article_type = input()
web_page_scraper(url, n_pages, article_type)
