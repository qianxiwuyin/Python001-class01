# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter





# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# useful for handling different item types with a single interface
class WangpinPipeline():
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='zt123666',
            database='douban_short',
            charset='utf8mb4'
        )
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        # 游标建立的时候就开启了一个隐形的事物
        movie_name = item['movie_name']
        start_title = item['start_title']
        short = item['short']
        #数据库断开的时候再次链接
        self.conn.ping(reconnect=True)
        sqls='insert into douban_short.tb_movies(movie_name,short,start_title)' \
             'values(%s,%s,%s);'
        try:
            if self.cur.execute(sqls,(movie_name,short,start_title)):
                print('插入成功')
                self.conn.commit()
        except:
            print('插入失败')
            self.conn.rollback()
            self.conn.ping(reconnect=True)
        self.conn.close()
        return item



