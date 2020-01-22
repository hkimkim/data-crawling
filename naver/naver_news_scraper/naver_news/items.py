# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class NaverNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    userName = scrapy.Field(output_processor=TakeFirst())
    date = scrapy.Field(output_processor=TakeFirst()) #modTimeGmt
    title = scrapy.Field(output_processor=TakeFirst())
    press = scrapy.Field(output_processor=TakeFirst())
    content = scrapy.Field(output_processor=TakeFirst())
    likes = scrapy.Field(output_processor=TakeFirst()) #sympathyCount
    dislikes = scrapy.Field(output_processor=TakeFirst()) #antipathyCount
    sad = scrapy.Field(output_processor=TakeFirst()) # 슬퍼요
    like = scrapy.Field(output_processor=TakeFirst()) #좋아요
    angry = scrapy.Field(output_processor=TakeFirst()) #화나요
    want = scrapy.Field(output_processor=TakeFirst()) #후속기사 원해
    warm = scrapy.Field(output_processor=TakeFirst()) #훈훈해요
