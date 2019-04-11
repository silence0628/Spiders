#coding:utf-8
"""
    百度贴吧　壁纸
    date: 20190411
    author: huhaohang
"""
import requests
from bs4 import BeautifulSoup
import urllib.request
import time

def getHtml(url):
    html = requests.get(url)
    # html = html.read()
    return html

base_url = 'http://tieba.baidu.com/p/6038328054'
html = getHtml(base_url)
soup = BeautifulSoup(html.text, 'lxml')
k = 1
for i in soup.find_all('img',{'class':"BDE_Image"}):
    print(i['src'])
    time.sleep(2)
    urllib.request.urlretrieve(i['src'], './data/iu{:0>3}.jpg'.format(str(k)))
    k += 1