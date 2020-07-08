import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd

url = 'https://maoyan.com/films?catId=3&showType=3&offset=30'

User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
Cookie='__mta=120028983.1593306417025.1593328161781.1593328782311.6; uuid_n_v=v1; uuid=A8E24090B8DB11EA97185D50074468A7AD136205F3834F5588B9FFE0B8978DFB; _csrf=2ba9f02a91105f6413cf4a4b471ec45e80a5aa26ed18d6a66837decbd673ac03; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593306417; mojo-uuid=9a19d0f417bd6ba12509d96bc0f89e3b; _lxsdk_cuid=172f8768738c8-0d70d070e88c78-4353760-1fa400-172f8768738c8; _lxsdk=A8E24090B8DB11EA97185D50074468A7AD136205F3834F5588B9FFE0B8978DFB; mojo-session-id={"id":"ff9cc14c607982f5f9b67cd983da1b3e","time":1593328161635}; mojo-trace-id=5; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593329047; __mta=120028983.1593306417025.1593328782311.1593329047002.7; _lxsdk_s=172f9c250de-024-d31-ab9%7C%7C11'
header = {'User-Agent':User_Agent,'Cookie':Cookie}
res = requests.get(url=url,headers=header)
selector = lxml.etree.HTML(res.text)

bs_info = bs(res.text, 'html.parser')

#获取电影名称
file_name = selector.xpath('//div[@class="movie-hover-title"]/span[contains(@class,"name ")]/text()')
print(f'电影名称：{file_name}')
#获取电影类型
tag = selector.xpath('//span[contains(text(),"类型:")]/following-sibling::node()')
#去除回车
type = [x.strip() for x in tag if x.strip()!='\n']
print(f'电影类型：{type}')
#获取上映日期
date = selector.xpath('//span[contains(text(),"上映时间:")]/following-sibling::node()')
dates = [y.strip() for y in date if y.strip()!='\n']
print(f'上映日期：{dates}')

# 将数据存放到列表里面
mylist = [file_name, type, dates]
movie1 = pd.DataFrame(data=mylist)
movie1 = movie1.sort_values(by=0, axis=0)

# windows需要使用gbk字符集
movie1.to_csv('./moviedata.csv', encoding='gbk', index=False, header=False)
# 控制请求的频率，引入了time模块
from time import sleep

sleep(10)


