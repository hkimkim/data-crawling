# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MovieCodePipeline(object):
    def process_item(self, item, spider):
        code = [re.findall('[0-9]+', i)[0] for i in code_url]
        return item
