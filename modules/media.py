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
    song_name = res.json()['title']
    song_name = os.path.abspath('') + 'songs/' + song_name  + '.mp3'
    if os.path.isfile(song_name):
        return song_name
    else:
        res = requests.get(link)
        file = open(song_name, 'wb')

        for i in res.iter_content(10000):
            file.write(i)

        file.close()
        return song_name


# def download_video(yt_link):
#     try:
#         link = 'http://youtubeinmp4.com/youtube.php?video=' + yt_link
#
#         res = requests.get(link)
#         soup = BS(res.text, 'html.parser')
#         elem = soup.find('a', {'class': 'downloadButtons btn btn-lg btn-block btn-success borderBottom'})
#         print elem
#         download_link = 'http://youtubeinmp4.com/' + elem['href']
#         print(download_link)
#
#         temp = soup.find('h2').text
#
#         video_name = ''
#         for i in temp:
#             if i in string.ascii_letters + '()-_ ':
#                 video_name += i
#
#         video_name = os.path.abspath('~')[:-1] + 'videos/' + video_name + '.mp4'
#         if os.path.isfile(video_name):
#             return video_name
#         res = requests.get(download_link)
#         file = open(video_name, 'wb')
#
#         for i in res.iter_content(10000):
#             file.write(i)
#
#         file.close()
#         return video_name
#     except Exception as e:
#         print traceback.print_exc()
#         print(e , 'exception')
#         raise RuntimeError