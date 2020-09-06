# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class PhotoPipeline():
    def __init__(self):
        self.conn = pymysql.connect(
            port=3306,
            user='root',
            password='zt123666',
            database='szdata',
            charset='utf8mb4'
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        # 游标建立的时候就开启了一个隐形的事物
        title = item['title']
        author = item['author']
        description = item['description']
        time = item['time']
        commentnum = item['commentnum']
        # 数据库断开的时候再次链接
        self.conn.ping(reconnect=True)
        sqls = 'insert into szdata.old_szdata(title,author,description,time)' \
               'values(%s,%s,%s,%s);'
        sqlone = 'insert into szdata.commentnum(title,commentnum)' \
              'values(%s,%s);'
        try:
            if self.cur.execute(sqls, (title, author,description,time)):
                print('插入成功')
                self.conn.commit()
            if self.cur.execute(sqlone, (title, commentnum)):
                print('插入成功')
                self.conn.commit()
        except:
            print('插入失败')
            self.conn.rollback()
            self.conn.ping(reconnect=True)
        self.conn.close()
        return item

    # Define your item pipelines here
    #
    # Don't forget to add your pipeline to the ITEM_PIPELINES setting
    # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

    # useful for handling different item types with a single interface

'''
import csv
class PhotoPipeline():
    def process_item(self, item, spider):
        title = item['title']
        description = item['description']
        author = item['author']
        output = f'{title}\t,{author}\t,{description}\t\n'
        with open('./test.csv', 'a+', encoding='utf-8-sig') as article:
            article.write(output)
            # article.close()
        return item
'''
