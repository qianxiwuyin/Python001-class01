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


for tags in bs_info.find_all('div',attrs={'class':'movie-item-hover'}):
    for atags in tags.find_all('a',):
        file_name='https://maoyan.com'+atags.get('href')
        print(file_name)
        for btags in atags.select('div[class="movie-hover-title movie-hover-brief"]'):
            title=btags.get('title')
            print(title)
            for ctags in btags.select('div[class="movie-hover-title movie-hover-brief"]>span.hover-tag'):
                dates=ctags.next_sibling.strip()
                print(dates)
                #next_sibling 查找下一个元素
                output = f'{title}\t,{file_name}\t,{dates}\t\n'
                with open('./maoyanmovie.csv', 'a+', encoding='utf-8-sig') as article:
                    article.write(output)



