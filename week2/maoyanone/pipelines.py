# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
class MaoyanonePipeline():
    def __init__(self):
        self.conn = pymysql.connect(
            port=3306,
            user='root',
            password='zt123',
            database='geektime_python_train',
            charset='utf8mb4'
        )
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        # 游标建立的时候就开启了一个隐形的事物
        title = item['title']
        type = item['type']
        date = item['date']
        #数据库断开的时候再次链接
        self.conn.ping(reconnect=True)
        sqls='insert into geektime_python_train.week02_maoyan_movie(movie_name,movie_type,movie_showtime)' \
             'values(%s,%s,%s);'
        try:
            if self.cur.execute(sqls,(type,title,date)):
                print('插入成功')
                self.conn.commit()
        except:
            print('插入失败')
            self.conn.rollback()
            self.conn.ping(reconnect=True)
        self.conn.close()
        return item


