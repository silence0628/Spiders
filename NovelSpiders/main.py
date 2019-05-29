#coding:utf-8
"""
    笔趣阁 小说  https://www.sbiquge.com/0_466/   如：0_466代表辰东的《遮天》
    date: 20190529
    author: huhaohang
"""
import requests
from bs4 import BeautifulSoup
import urllib.request
import time
import argparse
import os
import random



parser = argparse.ArgumentParser(description='')
parser.add_argument('--path', dest='path', default='./txt', help='整本小说txt存储路径')
parser.add_argument('--filename', dest='filename', default='遮天.txt', help='小说名称')
parser.add_argument('--novel_index', dest='novel_index', default='0_466', help='笔趣阁小说序列号，如 466 for 遮天')
args = parser.parse_args()

def getMainHtml(url):
    html = requests.get(base_url)
    soup = BeautifulSoup(html.text, 'lxml')
    time.sleep(random.randint(2, 4))

    indexs = soup.find('div', class_="listmain")
    indexs = indexs.find_all('dd')

    titles = []
    urls = []
    for index in indexs:
        # print(index.a.string)
        # print('https://www.sbiquge.com' + index.a['href'])
        # print('*' * 30)

        urls.append('https://www.sbiquge.com' + index.a['href'])
        titles.append(index.a.string)

    return urls, titles

def main(base_url):

    urls, titles = getMainHtml(base_url)

    filename = args.filename
    with open(filename, 'a', encoding='utf-8') as file:
        for i in range(len(urls)):
            # print(urls[i])
            print(titles[i])
            result = parseHtml(urls[i])
            result.insert(0, titles[i]+'\n\n')
            # time.sleep(random.randint(4, 6))
            for j in result:
                file.write(j)

def parseHtml(singleUrl):
    """
    :param singleUrl: https://www.sbiquge.com/0_466/253544.html
    :return:
    """
    time.sleep(random.randint(0, 1))
    html = requests.get(singleUrl)
    soup = BeautifulSoup(html.text, 'lxml')
    txt = soup.find('div', class_="showtxt")

    result = [txt.text.replace(' ', '\n')]

    return result

if __name__ == '__main__':
    base_url = 'https://www.sbiquge.com/' + args.novel_index
    if not os.path.exists(path=args.path):
        os.mkdir(args.path)

    main(base_url)



