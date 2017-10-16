from bs4 import BeautifulSoup as BS
import requests , random

def rand_jokes():
    jokeurl = 'https://www.rd.com/jokes/family/'
    res = requests.get(jokeurl)
    soup = BS(res.text,'html.parser')
    result = soup.find_all('div', {'class':'jokes-river--content'})
    return random.choice(result).text