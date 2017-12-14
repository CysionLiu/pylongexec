import json

from bs4 import BeautifulSoup as soup
import requests


def get_all(url):
    result = requests.get(url)
    result.encoding = 'utf-8'
    content = result.text
    return content


def get_body(url):
    content = get_all(url)
    content = soup(content, 'html.parser')
    return content


def get_simple_lists(url):
    body = get_body(url)
    L = body.select('.news-item')
    for news in L:
        h2 = news.select('h2')
        if len(h2) > 0:
            h2, link, time = news.select('h2')[0].text, news.select('a')[0]['href'], \
                             news.select('.time')[0].text
            # print(h2, link, time)


def get_inner(url):
    body = get_body(url)
    article_title = body.select('.main-title')[0].text
    print(article_title)
    data_src = body.select('.date-source')[0].select('a')[0].text
    print(data_src)
    ctime = body.select('.date')[0].text
    print(ctime)
    artciles = body.select('.article')[0].select('p')
    for a in artciles[:-1]:
        print(a.text.strip())
    editor = body.select('.show_author')[0].text.lstrip('责任编辑：')
    print(editor)


def get_comment(url):
    body = get_body(url)
    jsons = json.loads(body.text.lstrip('jsonp_1513242542440(').rstrip(')'))
    comment_count = jsons['result']['count']['total']
    print(comment_count)


if __name__ == '__main__':
    url = 'http://news.sina.com.cn/china/'
    url2 = 'http://news.sina.com.cn/o/2017-12-14/doc-ifyptfcn0287301.shtml'
    url_com = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=sh&newsid=comos-fypsvkp2763006&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1&callback=jsonp_1513242542440&_=1513242542440'
    # get_simple_lists(url)
    get_inner(url2)
    get_comment(url_com)
