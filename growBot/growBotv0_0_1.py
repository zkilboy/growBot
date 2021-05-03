#! Python3

#growBot: House Plant Life Support

from bs4 import BeautifulSoup as bs
import requests

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

def weatherPull(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    html = session.get(url)
    print(html.text)

weatherPull("https://www.weather.com")