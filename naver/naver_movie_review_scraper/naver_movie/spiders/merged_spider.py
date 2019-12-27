import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from datetime import datetime
from naver_movie.items import NaverMovieItem, MovieCodeItem, ReviewCount
import re
import math

#this code crawls the user movie review from naver's 2000 movie rank

class MergedSpider(scrapy.Spider):
    name = "merged_spider"
    max_page = 40 #number of pages from ranking pages
    now = datetime.now()
    date = now.strftime("%Y%m%d") #today's date

    def start_requests(self):
        #request the page with the ranking
         for i in range(self.max_page):
             yield Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date={0}&page={1}'.format(self.date,i), callback=self.code_parse )

    #scrape the movie code from movie review url
    def code_parse(self,response):
        movie_title = response.css("td.title div.tit5 a::attr(title)").extract()
        movie_code_url = response.css("td.title div.tit5 a::attr(href)").extract()

        #extract only the movie code from url
        movie_codes = [re.findall('[0-9]+', i)[0] for i in movie_code_url]

        for n in range(len(movie_codes)):
            #save the scraped movie_code and movie_title into dataframe called MovieCodeItem
            FirstItem = MovieCodeItem()
            FirstItem['title'] = movie_title[n]
            FirstItem['code'] = movie_codes[n]

            #send request to each movie page
            yield Request("https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={0}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1".format(movie_codes[n]), callback=self.review_count_parse, meta={'FirstItem': FirstItem})

    #scrape the total number of user movie reviews from each movie page
    def review_count_parse(self,response):
        total_reviews = response.css("div.score_total strong.total em::text").extract()[0].replace(",","")
        first_item = response.meta.get('FirstItem') #data from the first request (code_parse)
        movie_code = first_item['code']
        movie_title = first_item['title']

        #divide the total number of user movie reviews into 10 as each user movie review page has maximum 10 reviews
        for i in range(0, math.ceil(int(total_reviews)/10)+1):
            #send request to page with user movie reviews
            yield Request('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={0}&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=sympathyScore&page={1}'.format(movie_code, i), callback=self.reviews_parse, cb_kwargs = {'title': movie_title})

    #scrape the written review and the user, date, star_score, likes and dislikes of the written review from each review page
    def reviews_parse(self, response, title):
        user = response.css('div.score_reple dt em a span::text').extract()
        date = response.css('div.score_reple dt em:last-child::text').extract()
        reviews = ["".join(response.css('div.score_reple p span#_filtered_ment_'+str(n)+"::text").extract()).strip().replace("\n", " ").replace("\r", " ") for n in range(len(user))]
        star_score = response.css('div.star_score em::text').extract()
        likes = response.css('a._sympathyButton strong::text').extract()
        dislikes = response.css('a._notSympathyButton strong::text').extract()

        all = list(zip(user, date, reviews, star_score, likes, dislikes))

        for n in range(len(all)):
            #save the scraped items into dataframe called NaverMovieItem
            item = ItemLoader(item=NaverMovieItem())
            item.add_value('title', title)
            item.add_value('user', all[n][0])
            item.add_value('date', all[n][1])
            item.add_value('reviews', all[n][2])
            item.add_value('star_score', all[n][3])
            item.add_value('likes', all[n][4])
            item.add_value('dislikes', all[n][5])

            yield item.load_item()
