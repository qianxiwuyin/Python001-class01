import scrapy
from photo.items import PhotoItem
from scrapy import Selector


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['www.smzdm.com']
    start_urls = ['https://www.smzdm.com/']

    def start_requests(self):
        for i in range(1,5):
            url = f'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p'+str(i)+'/#feed-main'
            print(url)
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)
    def parse(self, response):
        item = PhotoItem()
        mobilephoto = Selector(response=response).xpath('//*[@class="z-feed-content "]')
        for tag in mobilephoto:
                link = tag.xpath('./h5[@class="feed-block-title"]/a/@href').extract()[0]
                #获取链接和手机标题
                item['link']=link
                yield scrapy.Request(url=link, meta={'item': item }, callback=self.parse2)
    def parse2(self,response):
        item = response.meta['item']
        mobilephoto2 = Selector(response=response).xpath('//*[@id="feed-main"]')
        for tags in mobilephoto2:
                title = tags.xpath('//h1[@class="title J_title"]/text()')
                author = tags.xpath('//*[@class="comment_conBox"]/div[@class="comment_avatar_time "]/'
                                '/a[@class="a_underline user_name"]/span/text()')
                description =tags.xpath('//*[@class="comment_conBox"]/div[@class="comment_conWrap"]/'
                                    'div[@class="comment_con"]/p/span/text()')
                time = tags.xpath('//*[@class="comment_conBox"]/div[@class="comment_avatar_time "]/'
                              'div[@class="time"]/meta/@content')
                commentnum=tags.xpath('//section[@id="comments"]/div[@id="panelTitle"]/em/text()')
                #获取评价用户名，用户评价内容，评价时间
                item['title'] = title.extract_first().strip()
                item['author'] = author.extract_first().strip()
                item['description'] = description.extract_first().strip()
                item['time']= time.extract_first().strip()
                item['commentnum']=commentnum.extract_first().strip()
                yield item












