import scrapy
from scrapy.http import Request
from naver_news.items import NaverNewsItem
from scrapy.loader import ItemLoader
import json
import re

#this code crawls user comments from naver news articles

class NewsCommentSpider(scrapy.Spider):
    name = "news_comment_spider"
    #input news article you want to crawl
    url = "https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=437&aid=0000227434&date=20191226&type=2"

    oid = re.findall(r'(?<=&oid=)[0-9]+', url)[0]
    aid = re.findall(r'(?<=&aid=)[0-9]+',url)[0]

    def start_requests(self):
        yield Request(self.url, callback=self.basic_info_parse)

    #this code scrapes the title and press of the news article
    def basic_info_parse(self,response):
        title = response.css('div.article_header div.article_info h3#articleTitle::text').extract()[0]
        press = response.css('div.article_header div.press_logo img::attr(title)').extract()[0]

        BasicItem = NaverNewsItem()
        BasicItem['title'] = title
        BasicItem['press'] = press

        url ="https://apis.naver.com/commentBox/cbox/web_neo_list_jsonp.json?ticket=news&templateId=default_life&pool=cbox5&_callback=jQuery1124026940488629010395_1577777017437&lang=ko&country=KR&objectId=news"+self.oid+"%2C"+self.aid+"&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=1&initialize=true&userType=&useAltSort=true&replyPageSize=20&moveTo=&sort=favorite&includeAllStatus=true&_=1577777017438"
        header = {"referer":self.url}

        yield Request(url,callback=self.num_parse, headers=header, meta={'BasicItem': BasicItem})

    #this code scrapes the total number of user comments
    def num_parse(self, response):
        data = re.findall(r'(?<=jQuery)[0-9]*_[0-9]*(.*)', response.text)[0].replace("(","").replace(")","").replace(";","")
        jsonresponse = json.loads(data)
        total_page = jsonresponse['result']['pageModel']['totalPages']
        BasicItem = response.meta.get('BasicItem')

        for n in range(1,total_page+1):
            url ="https://apis.naver.com/commentBox/cbox/web_neo_list_jsonp.json?ticket=news&templateId=default_society&pool=cbox5&_callback=jQuery1707138182064460843_1523512042464&lang=ko&country=&objectId=news"+self.oid+"%2C"+self.aid+"&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page={0}&refresh=false&sort=FAVORITE".format(n)
            header = {"referer":url}
            yield Request(url,callback=self.parse, headers=header,meta={'BasicItem': BasicItem})

    #this code scrapes the user comment and other info of user comment from API (in json format)
    def parse(self, response):
        data = re.findall(r'(?<=jQuery)[0-9]*_[0-9]*(.*)', response.text)[0].replace("(","").replace(")","").replace(";","")
        jsonresponse = json.loads(data)
        BasicItem = response.meta.get('BasicItem')

        for ticket in jsonresponse['result']['commentList']:
            item = ItemLoader(item=NaverNewsItem())
            item.add_value('content', "".join(ticket['contents']).strip().replace("\n", " ").replace("\r", " "))
            item.add_value('likes', ticket['sympathyCount'])
            item.add_value('dislikes', ticket['antipathyCount'])
            item.add_value('userName', ticket['userName'])
            item.add_value('date',ticket['modTimeGmt'] )
            item.add_value('title', BasicItem['title'])
            item.add_value('press', BasicItem['press'])

            yield item.load_item()
