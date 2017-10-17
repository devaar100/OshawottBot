import requests
from bs4 import BeautifulSoup as BS
import random


def get_quotes():
    req = 'https://www.brainyquote.com/quotes/keywords/smart.html'
    res = requests.get(req)
    soup = BS(res.text, 'html.parser')
    list = [x.text for x in soup.find_all('a',{'class':'b-qt'})]
    return random.choice(list)