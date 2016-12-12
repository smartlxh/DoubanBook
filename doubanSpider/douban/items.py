# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    bookName = scrapy.Field()
    author = scrapy.Field()
    country = scrapy.Field()
    pub = scrapy.Field()
    price = scrapy.Field()
    dat = scrapy.Field()
    score = scrapy.Field()
    imgUrl = scrapy.Field()
    detailUrl = scrapy.Field()
    description = scrapy.Field()
