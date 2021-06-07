#!/usr/bin/env python3
import json
import requests
from bs4 import BeautifulSoup
import string
import os


def get_content_type(address):
    quote = address.split("/")[-1]
    r = requests.get(address)
    if r.status_code == 200:
        body = json.loads(r.content)
        if quote in body.values():
            content = r.content
        else:
            content = 'Invalid quote resource!'
    else:
        content = 'Invalid quote resource!'
    print(content)


def get_movie_description(movie_link):
    r = requests.get(movie_link, headers={'Accept-Language': 'en-US,en;q=0.5'})
    content = BeautifulSoup(r.content, 'html.parser')
    title = content.title.text
    imdb = content.find('meta', {'property': "imdb:pageType"})
    description = content.find('meta', {'name': 'description'})
    if description is not None:
        description = content.find('meta', {'name': 'description'}).get('content')
    summary = {'title': title, 'description': description}
    if description is None or imdb is None:
        print('Invalid movie page!')
    else:
        print(summary)


def save_url_content(link):
    r = requests.get(link)
    if r.status_code == 200:
        content = r.content
        with open('source.html', 'wb') as source:
            source.write(content)
        print('Content saved.')
    else:
        print(f'The URL returned {r.status_code}')


def web_scraper(link):
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    rm_punctuation = str.maketrans("", "", string.punctuation)
    for article in soup.find_all('article'):
        if article.find('span', {'data-test': 'article.type'}).find('span', {'class': 'c-meta__type'}).text == 'News':
            link_article = 'https://www.nature.com' + \
                           article.find('a', {'data-track-action': 'view article'}).get('href')
            article_content = BeautifulSoup(requests.get(link_article).content, 'html.parser')
            article_title = article_content.title.text.translate(rm_punctuation).strip().replace(' ', '_') + '.txt'
            body = article_content.find('div', {'class': 'c-article-body'}).text.strip().encode('utf-8')
            with open(file=article_title, mode='wb') as file:
                file.write(body)


def web_page_scraper(link, n_pages, article_type):
    rm_punctuation = str.maketrans("", "", string.punctuation)
    for n in range(n_pages):
        url_page = link + f'?searchType=journalSearch&sort=PubDate&page={n + 1}'
        soup = BeautifulSoup(requests.get(url_page).content, 'html.parser')
        os.mkdir(f'Page_{n + 1}')
        for article in soup.find_all('article'):
            if article.find('span', {'data-test': 'article.type'}).find('span', {'class': 'c-meta__type'}).text == f'{article_type}':
                link_article = 'https://www.nature.com' + \
                               article.find('a', {'data-track-action': 'view article'}).get('href')
                article_content = BeautifulSoup(requests.get(link_article).content, 'html.parser')
                article_title = article.find(class_='c-card__title').text.translate(rm_punctuation).strip().replace(' ', '_') + '.txt'
                if article_content.find('div', {'class': 'article-item__body'}):
                    body = article_content.find('div', {'class': 'article-item__body'}).text.strip().encode('utf-8')
                else:
                    body = article_content.find('div', {'class': 'c-article-body'}).text.strip().encode('utf-8')
                article_path = f'Page_{n + 1}/' + article_title
                with open(file=article_path, mode='wb') as file:
                    file.write(body)
    print('Saved all articles')
