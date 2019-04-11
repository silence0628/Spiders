#coding:utf-8
"""
    南京　算法工程师　岗位信息
    date: 20190411
    author: huhaohang
"""
import re
import time
import random
from urllib.request import urlopen
import requests
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from requests.exceptions import RequestException

import warnings
warnings.filterwarnings('ignore')

# 南京站的基础url

base_url = 'https://tieba.baidu.com/p/6088563735'

# 请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def getHtml(url):
    html = requests.get(url)
    # html = html.read()
    return html


html = getHtml(base_url)
soup = BeautifulSoup(html.text, 'lxml')
for i in soup.find_all('img',{'class':"BDE_Image"}):
    print(i,'\n')