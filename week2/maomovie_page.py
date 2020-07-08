# 翻页的处理

import requests
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装

# Python 使用def定义函数，myurl是函数的参数
url = 'https://maoyan.com/films?catId=3&showType=3&offset=30'
#def get_url_name(myurl):
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
header = {'user-agent':User_Agent}
header = {'User-Agent':User_Agent,'cookies':Cookie}
res = requests.get(url=url,headers=header)
print(res.text)
bs_info = bs(res.text, 'html.parser')
title = bs_info.find_all('div',attrs={'class':['channel-detail movie-item-title']}).find('a').text
    #date = bs_info.find_all('span',attrs={})




print(url)
 # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
'''
    for tags in bs_info.find_all('dd'):
         for atag in tags.find_all('a'):
            # 获取所有链接
            print(atag.get('href'))
            # 获取电影名字
            print(atag.find(attrs={'class':'name'}).text()


# 生成包含所有页面的元组
urls = tuple(f'https://maoyan.com/films?catId=3&showType=3&offset={i*30}' for i in range(10))

print(urls)

# 控制请求的频率，引入了time模块
from time import sleep

sleep(1)

for i in urls:
    get_url_name(i)
    sleep(5)'''
