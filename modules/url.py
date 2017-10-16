import requests
import json
import os

def shorten_url(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key={}'.format(os.environ['GURL'])
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    return (r.json())['id']