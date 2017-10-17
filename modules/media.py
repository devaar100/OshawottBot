import requests
from bs4 import BeautifulSoup as BS


def find_song(songname):
    req = 'https://www.youtube.com/results?search_query='+songname
    resp = requests.get(req)
    soup = BS(resp.text, 'html.parser')
    list = ['https://www.youtube.com'+str(x['href']) for x in soup.find_all('a',{'class':' yt-uix-sessionlink spf-link '})]
    return list