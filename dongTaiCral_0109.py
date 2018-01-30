#coding:utf-8
"""
    练习动态加载Ajax类型的数据网站的爬取，如 百度图片之类的
    主要工具为   selenium 搭载  phantomjs   模拟浏览器动态加载
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

#%%
"""#####################################################################################################################################################################"""
"""  1 传统方法  爬取，，获得  【】
    test 会发现得到 空矩阵，没有任何内容，但是在源码中是能够看见的我们所需要爬取的数据链接，此时这就是 网站采用了动态加载技术"""
# import requests
#
# url = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1515494057630_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1515494057632%5E00_611X954&word=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0'
# html = requests.get(url)
# print(html)
# soup = BeautifulSoup(html.text,'lxml')
# # print(soup)
# company_list = soup.find_all("li",class_="imgitem")
# print(company_list)
# <Response [200]>
# []
"""#####################################################################################################################################################################"""
#%%
""" 2 简单的抓包技术，也是没法能够很好的解决，，而下面 的方法唯一的缺陷就是  抓取速度会偏慢，，模仿浏览器行为"""
driver = webdriver.PhantomJS(executable_path="D:\\360Downloads\phantomJS\phantomjs-2.1.1-windows\\bin\phantomjs.exe")
# driver.get("http://www.baidu.com/")
#
# searchInput = driver.find_element_by_id('kw')    #通过ID定位
# searchInput.send_keys("python")
#
# searchSubmitBtn = driver.find_element_by_id("su")
# searchSubmitBtn.submit() #  模拟提交表单
#
# # 因为百度的搜索是异步的
# # 我们这里设置等待20秒
# # 如果网页标题中包含了"python" 我们就认为加载成功了
# WebDriverWait(driver,20).until(expected_conditions.title_contains("python"))
# # print(driver.title) # python_百度搜索
# html = driver.page_source
# soup = BeautifulSoup(html,'lxml')
# print(soup)
#%%
driver = webdriver.PhantomJS(executable_path="D:\\360Downloads\phantomJS\phantomjs-2.1.1-windows\\bin\phantomjs.exe")
def search(keyword,pages):
    
    
    totalPages = int(pages)*20
    url_keyword = urllib.parse.quote(keyword)
    urls_mat = []
    
    k = 0
    
    for page in range(0,totalPages,20):
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + url_keyword + '&pn=' + str(page) + '&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0'
        print(url)
        if url:
            time.sleep(5)
            driver.get(url)
            bsObj = BeautifulSoup(driver.page_source, "html5lib")
    #        print(bsObj)
            company_list = bsObj.find_all("li",class_="imgitem")
            
            print("*********************************************%d***************************************************************************************************"%k)
            print(len(company_list))
            for company in company_list:
                link = company.img['src']
                print(link)
                urls_mat.append(link)
            
            k+=1
        else:
            print('当前页面不存在')
        
    return urls_mat
if __name__ == '__main__':
    keywords = input('please input the key word:')
    k = input('please input the crawl page:')
    urls = search(keyword=keywords,pages=k)

"""down the pictures"""

from urllib import request
import socket
socket.setdefaulttimeout(30)

nums = len(urls)

for k in range(nums): 
    #生成一张壁纸的地址
    url = urls[k]
    if url:
        print(url)
        #爬取一张壁纸
        try:
            time.sleep(1)
            imagename='E:\\HHH\\Spiders\\dongTaiCrawl\\胡歌'+'\\'+'胡歌_' + str(k) + '.jpg' 
            request.urlretrieve(url,imagename)
        except:
            print(None)
    else:
        print('url link is error!!!')
#%%
"""批量更改文件名replace the name"""
import os

total = os.listdir('E:\HHH\Spiders\\dongTaiCrawl\倪妮')
for i in total:
    one = i.replace("倪妮", "迪丽热巴")
#    print(one)
    os.rename('E:\HHH\Spiders\\dongTaiCrawl\倪妮\\'+i,'E:\HHH\Spiders\\dongTaiCrawl\倪妮\\'+one)        