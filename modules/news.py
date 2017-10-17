import requests
import os


def get_news():
    newsurl = 'https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey={}'.format(os.environ['NURL'])
    resp = (requests.get(newsurl)).json()['articles']
    list = []
    for news in resp:
        list.append(news['url'])
    return list
