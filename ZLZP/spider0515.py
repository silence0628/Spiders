import requests
import time
from bs4 import BeautifulSoup
import random
import urllib.parse
import argparse
from glob import glob

#soup = BeautifulSoup(content, 'lxml')
#result = soup.find_all('ul', class_='searchResultListUl')
#
#result_list = result[0].find_all('li')
#
#for one in result_list:
#    
#    print('*'*100)
#    
#    company_name = one.find('p', class_='searchResultCompanyname').string
#    print('公司名称：%s'%company_name)
#    
#    company_address = one.find('em', class_='searchResultJobCityval').string
#    print('公司地址：%s'%company_address)
#    
#    jobdescrption = one.find('p', class_='searchResultJobdescription').find('span').string
#    print('职位需求：%s'%jobdescrption, '\n')

parser = argparse.ArgumentParser(description='')
parser.add_argument('--job_name', dest='job_name', default='算法工程师', help='job name')
parser.add_argument('--pages', dest='pages', type=int, default=10, help='job pages')
args = parser.parse_args()



def parseSingleUrl(url_name):
    # 解析公司页面
    url_name = 'https:'+ url_name
    
    content = requests.get(url_name).text
    soup = BeautifulSoup(content, 'lxml')
    result = soup.find_all('div', class_="cLeft l")
    
    return result

def parseSinglePage(url):
    # 解析某类职位的页面
    html = requests.get(url)
    content = html.text
    
    soup = BeautifulSoup(content, 'lxml')
    result = soup.find_all('ul', class_='searchResultListUl')[0]
    result_list = result.find_all('div', class_="searchResultItemDetailed")
    
    for one in result_list:
        print('*'*20)
        time.sleep(random.randint(2,8))
        url_name = one.a['href']    
        res = parseSingleUrl(url_name=url_name)[0]
        
        company_name = res.find('li', class_='cJobDetailInforWd1 marb').a.string
        print('公司名称： re%s'%company_name)
        
        company_addr = res.find_all('li', class_="cJobDetailInforWd2 marb")[0]['title']
        print('公司地址： %s'%company_addr)
        
        job_name = res.find_all('li', class_="cJobDetailInforWd2 marb")[1].string
        print('职位名称： %s'%job_name)
    
        person = res.find_all('li', class_="cJobDetailInforWd2 marb")[2].string
        print('招聘人数： %s'%person)
        
        date = res.find_all('li', class_="cJobDetailInforWd2 marb")[3].string
        print('公司地址： %s'%date)
        
        job_duty = res.find('p', class_="mt20").text.replace('\xa0', ' ')
        print('工作职责： %s'%job_duty.strip('岗位职责'))

def start():
    for i in range(args.pages):
        url = 'https://xiaoyuan.zhaopin.com/full/0/0_0_0_0_0_-1_{}_{}_0'.format(urllib.parse.quote(args.job_name), i)
        print('*'*100)
        parseSinglePage(url)
    
    
if __name__ == '__main__':

    start()