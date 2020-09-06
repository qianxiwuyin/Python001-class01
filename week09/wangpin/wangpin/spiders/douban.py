import scrapy
from wangpin.items import WangpinItem
from scrapy.selector import Selector

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/']
    def start_requests(self):
        for i in range(20):
            url = f'https://movie.douban.com/subject/1292214/comments?start={i}&limit=20&sort=new_score&status=P'
            yield scrapy.Request(url,callback=self.parse,dont_filter=True)
    def parse(self, response):
        item = WangpinItem()
        movies = Selector(response=response).xpath('//*[@id="content"]')
        for tag in movies:
            movie_name = tag.xpath('//h1/text()')
            start_title = tag.xpath('//*[@class="comment"]/h3/span[@class="comment-info"]/span[2]/@title')
            short = tag.xpath('//*[@id="comments"]//span[@class="short"]/text()')
            item['start_title']= start_title.extract_first().rstrip()
            item['short'] = short.extract_first().rstrip()
            item['movie_name'] = movie_name.extract_first().rstrip()
            yield item

