from bs4 import BeautifulSoup as BS
from modules.url import *
import requests

def find_lyrics(songname):
    url = 'https://search.azlyrics.com/search.php?q='+songname
    resp = requests.get(url)
    soup = BS(resp.text,'html.parser')
    items = soup.find_all('td',{'class':'text-left visitedlyr'})
    list = []
    for i in items[:3]:
        link = shorten_url(i.select('a')[0]['href'])
        list.append(
        str(i.select('a')[0].text)+'\n'+
        str(i.select('b')[1].text)+'\n'+
        str(link)
        )
    return list


# def download_lyrics(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
#     resp = requests.get(url=str(url),headers=headers,stream=True)
#     soup = BS(resp.text,'html.parser')
#     data = soup.find_all('div',{'class':'col-lg-8'})[0]
#     return data.select('div')[6].text


def find_song(songname):
    req = 'https://www.youtube.com/results?search_query='+songname
    resp = requests.get(req)
    soup = BS(resp.text, 'html.parser')
    list = ['https://www.youtube.com'+str(x['href']) for x in soup.find_all('a',{'class':' yt-uix-sessionlink spf-link '})]
    return list


def download_song(dlink):
    link = 'http://www.youtubeinmp3.com/fetch/?format=JSON&video=' + dlink
    res = requests.get(link)
    download_link = res.json()['link']
    song_name = res.json()['title']
    if os.path.isfile(song_name):
        return song_name
    else:
        res = requests.get(download_link)
        file = open(song_name, 'wb')
        for i in res.iter_content(10000):
            file.write(i)
        file.close()
        return song_name




