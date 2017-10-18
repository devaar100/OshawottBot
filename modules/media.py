import requests
import os
from bs4 import BeautifulSoup as BS


def find_song(songname):
    req = 'https://www.youtube.com/results?search_query='+songname
    resp = requests.get(req)
    soup = BS(resp.text, 'html.parser')
    list = ['https://www.youtube.com'+str(x['href']) for x in soup.find_all('a',{'class':' yt-uix-sessionlink spf-link '})]
    return list


def download_song(dlink):
    link = 'http://www.youtubeinmp3.com/fetch/?format=JSON&video=' + dlink
    res = requests.get(link)
    link = res.json()['link']
    return link

    # song_name = os.path.abspath('') + 'songs/' + song_name  + '.mp3'
    # if os.path.isfile(song_name):
    #     return song_name
    # else:
    #     res = requests.get(link)
    #     file = open(song_name, 'wb')
    #
    #     for i in res.iter_content(10000):
    #         file.write(i)
    #
    #     file.close()
    #     return song_name

