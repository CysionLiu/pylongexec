import re

import requests
from bs4 import BeautifulSoup as soup


def get_links(url):
    resp = requests.get(url)
    page = resp.text
    doc = soup(page)
    links = [ele.get('href') for ele in doc.find_all('a')]
    return links


if __name__ == '__main__':
    url = 'http://geek.csdn.net/mobile'
    links = get_links(url)
    for l in links:
        reg = re.compile(r'http(s)?')
        result = reg.search(str(l))
        if result is not None:
            print(l)
