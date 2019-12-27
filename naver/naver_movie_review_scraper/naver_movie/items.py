# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class NaverMovieItem(scrapy.Item):
    title = scrapy.Field(output_processor=TakeFirst())
    user = scrapy.Field(output_processor=TakeFirst())
    date = scrapy.Field(output_processor=TakeFirst())
    reviews = scrapy.Field(output_processor=TakeFirst())
    star_score = scrapy.Field(output_processor=TakeFirst())
    likes = scrapy.Field(output_processor=TakeFirst())
    dislikes = scrapy.Field(output_processor=TakeFirst())
    #url = scrapy.Field(output_processor=TakeFirst())

class ReviewCount(scrapy.Item):
    title = scrapy.Field()
    count = scrapy.Field()
    movie_code = scrapy.Field()
    #url = scrapy.Field()


class MovieCodeItem(scrapy.Item):
    title = scrapy.Field()
    code = scrapy.Field()
