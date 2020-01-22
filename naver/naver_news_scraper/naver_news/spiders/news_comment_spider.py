import scrapy
from scrapy.http import Request
from naver_news.items import NaverNewsItem
from scrapy.loader import ItemLoader
import json
import re

#this code scrapess user comments from naver news articles

class NewsCommentSpider(scrapy.Spider):
    name = "news_comment_spider"
    #input the news article link you want to scrape
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

        url = "https://news.like.naver.com/v1/search/contents?suppress_response_codes=true&callback=jQuery112409851002752979665_1579250003804&q=NEWS%5Bne_"+self.oid+"_"+self.aid+"%5D"

        yield Request(url,callback=self.reaction_parse, meta={'BasicItem': BasicItem})


    def reaction_parse(self, response):
        data = re.findall(r'(?<=jQuery)[0-9]*_[0-9]*(.*)', response.text)[0].replace("(","").replace(")","").replace(";","")
        jsonresponse = json.loads(data)
        BasicItem = response.meta.get("BasicItem")
        ReactionItem = NaverNewsItem()

        result = []
        for r in jsonresponse['contents'][0]['reactions']:
            result.append((r['reactionType'], r['count']))

        result = dict(result)

        for r in ["sad", "like", "angry", "want", "warm"]:
            if r not in result.keys():
                Reaction[r] = 0
            else:
                ReactionItem[r] = result[r]

        url ="https://apis.naver.com/commentBox/cbox/web_neo_list_jsonp.json?ticket=news&templateId=default_life&pool=cbox5&_callback=jQuery1124026940488629010395_1577777017437&lang=ko&country=KR&objectId=news"+self.oid+"%2C"+self.aid+"&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=1&initialize=true&userType=&useAltSort=true&replyPageSize=20&moveTo=&sort=favorite&includeAllStatus=true&_=1577777017438"
        header = {"referer":self.url}

        yield Request(url,callback=self.num_parse, headers=header, meta={'BasicItem': BasicItem, 'ReactionItem': ReactionItem})

    #this code scrapes the total number of user comments
    def num_parse(self, response):
        data = re.findall(r'(?<=jQuery)[0-9]*_[0-9]*(.*)', response.text)[0].replace("(","").replace(")","").replace(";","")
        jsonresponse = json.loads(data)
        total_page = jsonresponse['result']['pageModel']['totalPages']
        BasicItem = response.meta.get('BasicItem')
        ReactionItem = response.meta.get('ReactionItem')

        for n in range(1,total_page+1):
            url ="https://apis.naver.com/commentBox/cbox/web_neo_list_jsonp.json?ticket=news&templateId=default_society&pool=cbox5&_callback=jQuery1707138182064460843_1523512042464&lang=ko&country=&objectId=news"+self.oid+"%2C"+self.aid+"&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page={0}&refresh=false&sort=FAVORITE".format(n)
            header = {"referer":url}
            yield Request(url,callback=self.parse, headers=header,meta={'BasicItem': BasicItem, 'ReactionItem': ReactionItem})


    #this code scrapes the user comment and other info of user comment from API (in json format)
    def parse(self, response):
        data = re.findall(r'(?<=jQuery)[0-9]*_[0-9]*(.*)', response.text)[0].replace("(","").replace(")","").replace(";","")
        jsonresponse = json.loads(data)
        BasicItem = response.meta.get('BasicItem')
        ReactionItem = response.meta.get('ReactionItem')

        for ticket in jsonresponse['result']['commentList']:
            item = ItemLoader(item=NaverNewsItem())
            item.add_value('content', "".join(ticket['contents']).strip().replace("\n", " ").replace("\r", " "))
            item.add_value('likes', ticket['sympathyCount'])
            item.add_value('dislikes', ticket['antipathyCount'])
            item.add_value('userName', ticket['userName'])
            item.add_value('date',ticket['modTimeGmt'] )
            item.add_value('title', BasicItem['title'])
            item.add_value('press', BasicItem['press'])
            item.add_value('sad', ReactionItem['sad'])
            item.add_value('like', ReactionItem['like'])
            item.add_value('angry', ReactionItem['angry'])
            item.add_value('want', ReactionItem['want'])
            item.add_value('warm', ReactionItem['warm'])

            yield item.load_item()
