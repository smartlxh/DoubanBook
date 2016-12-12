# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
import traceback
class DoubanPipeline(object):

    def __init__(self):
        pass

    def open_spider(self, spider):


        config = {
          'host':'localhost',
          'port':3306,
          'user':'root',
          'password':'32784744li',
          'db':'douban',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor
          }
        self.connection = pymysql.connect(**config)


    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        try:
            with self.connection.cursor() as cursor:

                sql = 'INSERT INTO bookInfo (bookName,author,country,price,dat,score,description,imgUrl,detailUrl) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)'

                cursor.execute(sql,(item['bookName'],item['author'],item['country'],item['price'],item['dat'],item['score'],item['description'],item['imgUrl'],item['detailUrl']));
                self.connection.commit()
        except:
                traceback.print_exc()
                pass
        return item
