import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from naver_movie.items import NaverMovieItem
import re
import math

#this code crawls user movie reviews from naver movie review page
#this code crawls movie review of Frozen2

class ReviewSpider(scrapy.Spider):
    name = "review_spider"
    #input url of the movie
    url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=136873"

    def start_requests(self):
        yield Request(self.url, callback=self.general_info)

    def general_info(self, response):
        total_reviews = response.css("div.score div.score_total strong.total em::text").extract()[1].strip().replace(",","")
        movie_code = re.findall(r'(?<=code=)[0-9]+', self.url)[0]

        for n in range(0, math.ceil(int(total_reviews)/10)+1):
            yield Request('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={0}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={1}'.format(movie_code, n))

    #scrape the written review and the user, date, star_score, likes and dislikes of the written review from each review page
    def parse(self, response):
        user = response.css('div.score_reple dt em a span::text').extract()
        date = response.css('div.score_reple dt em:last-child::text').extract()
        reviews = ["".join(response.css('div.score_reple p span#_filtered_ment_'+str(n)+"::text").extract()).strip().replace("\n", " ").replace("\r"," ") for n in range(len(user)) ]
        star_score = response.css('div.star_score em::text').extract()
        likes = response.css('a._sympathyButton strong::text').extract()
        dislikes = response.css('a._notSympathyButton strong::text').extract()

        data = list(zip(user,date, reviews, star_score, likes, dislikes))

        item = ItemLoader(item = NaverMovieItem())

        for n in range(len(data)):
            item.add_value('username', data[n][0])
            item.add_value('date', data[n][1])
            item.add_value('reviews', data[n][2])
            item.add_value('star_score', data[n][3])
            item.add_value('likes', data[n][4])
            item.add_value('dislikes', data[n][5])

        yield item.load_item()
