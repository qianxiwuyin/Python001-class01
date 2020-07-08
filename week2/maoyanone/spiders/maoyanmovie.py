import scrapy
from maoyanone.items import MaoyanoneItem
from scrapy.selector import Selector

class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanmovie'
    allowed_domains = ['maoyan.com']
    #起始的url
    start_urls = ['https://maoyan.com/films/']

    #筛选数据
    def start_requests(self):
        for i in range(10):
            url = f'https://maoyan.com/films?showType=3&offset={i*30}'
            yield scrapy.Request(url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        item = MaoyanoneItem()
        movies = Selector(response=response).xpath('//dd')
        for movie in movies:
            title = movie.xpath('./div[@class="channel-detail movie-item-title"]/@title')
            #xpath 取同级目录下所有节点
            type = movie.xpath('//span[contains(text(),"类型:")]/following-sibling::node()')
            date = movie.xpath('//span[contains(text(),"上映时间:")]/following-sibling::node()')
            item['title'] = title.extract_first().strip()
            item['type'] = type.extract_first().strip()
            item['date'] = date.extract_first().strip()
            print("电影名称："+item['title'])
            print("电影类型："+item['type'])
            print("上映时间："+item['date'])
            yield item












