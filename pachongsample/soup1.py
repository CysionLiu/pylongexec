import re

import requests
from bs4 import BeautifulSoup as soup


def gethtml(url):
    resp = requests.get(url)
    page = resp.text
    contents = soup(page,"html.parser")
    return contents

def get_links(url):
    doc = gethtml(url)
    links = [ele.get('href') for ele in doc.find_all('a')]
    return links


if __name__ == '__main__':
    url = 'http://geek.csdn.net/mobile'
    links = get_links(url)
    print(gethtml(url))
    # for l in links:
    #     reg = re.compile(r'http(s)?')
    #     result = reg.search(str(l))
    #     if result is not None:
    #         print(l)
