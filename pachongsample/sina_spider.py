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


def get_article_detail(url):
    try:
        body = get_body(url)
        article_title = body.select('.main-title')[0].text
        data_src = body.select('.date-source')[0].select('a')[0].text
        ctime = body.select('.date')[0].text
        artciles = body.select('.article')[0].select('p')
        article_body = ''
        for a in artciles[:-1]:
            article_body += a.text.strip()
        editor = body.select('.show_author')[0].text.lstrip('责任编辑：')
        comment_count = get_comment(url)
        article = {'article_title': article_title, 'article_src': data_src, 'ctime': ctime,
                   'article_body': '暂不写入', 'editor': editor, 'comment_num': comment_count}
        # print(article)
        return article
    except:
        return None


def get_comment(url):
    import re
    rawurl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=sh&newsid=comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1'
    re_ids = re.search(r'doc-i(.*).shtml', url)
    newid = re_ids.group(1)
    url = rawurl.format(newid)
    body = get_body(url)
    try:
        jsons = json.loads(body.text)
        comment_count = jsons['result']['count']['total']
        return comment_count
    except:
        pass


def get_article_list(page):
    urls = []
    url = 'http://api.roll.news.sina.com.cn/zt_list?' \
          'channel=news&cat_1=gnxw&cat_2==gdxw1&level==1||=2&show_ext=1&show_all=1&show_num=22' \
          '&tag=1&format=json&page={}'
    url = url.format(page)
    jd = json.loads(get_body(url).text)
    a_list = jd['result']['data']
    for a in a_list:
        urls.append(a['url'])
        # print(a['title'])
    return urls


if __name__ == '__main__':
    # url = 'http://news.sina.com.cn/china/'
    # url2 = 'http://news.sina.com.cn/c/2017-12-12/doc-ifypnqvn3401389.shtml'
    # get_simple_lists(url)
    # get_article_detail(url2)
    # get_comment(url2)

    news_url_list = []
    news_list = []
    for i in range(1, 50):
        temp_L = get_article_list(i)
        if len(temp_L) < 1:
            pass
        news_url_list.extend(temp_L)
    for n in news_url_list:
        tmp = get_article_detail(n)
        if  tmp is not None:
            news_list.append(tmp)
            # print(a)
    import pandas

    df = pandas.DataFrame(news_list)
    df.to_excel('e:/tmp.xlsx')
    # print(df)
