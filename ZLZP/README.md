# 智联校园招聘职位爬虫

## 2019年5月15日 

对其进行网页源码查询，利用鼠标工具进行目标信息的查询

针对源码中，其网页格式源码设计，利用Python中爬虫工具库进行职位信息获取

项目配置环境：

    import requests              # 获取网页源码库
    import time                  # 时间库，sleep时间，防止爬虫被禁
    from bs4 import BeautifulSoup# bs库解析页面，排成统一格式
    import random
    import urllib.parse          # 对汉字编码，传入url
    import argparse              # 方便命令行传参，自定义
    from glob import glob

!(https://github.com/silence0628/Spiders/blob/master/ZLZP/IMGs/result1.png?raw=true)
!(https://github.com/youyou-579/123/blob/master/2.8.jpg?raw=true)