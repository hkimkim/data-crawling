import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
import math
from naver_movie.items import NaverMovieItem

#this code crawls user movie reviews from naver movie review page
#this code crawls movie review of Frozen2

class ReviewSpider(scrapy.Spider):
    name = "review_spider"
    total_reviews = 21278 #input the total number of reviews from the movie page
    movie_code = 136873 #input the movie code from the movie url
    item = ItemLoader(item = NaverMovieItem())

    #send request to each movie page
    def start_requests(self):
        for i in range(0, math.ceil(int(self.total_reviews)/10)+1):
            yield Request('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={0}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={1}'.format(self.movie_code, i))

    #scrape the written review and the user, date, star_score, likes and dislikes of the written review from each review page
    def parse(self, response):
        user = response.css('div.score_reple dt em a span::text').extract()
        date = response.css('div.score_reple dt em:last-child::text').extract()
        reviews = ["".join(response.css('div.score_reple p span#_filtered_ment_'+str(n)+"::text").extract()).strip().replace("\n", " ").replace("\r"," ") for n in range(len(user)) ]
        star_score = response.css('div.star_score em::text').extract()
        likes = response.css('a._sympathyButton strong::text').extract()
        dislikes = response.css('a._notSympathyButton strong::text').extract()

        data = list(zip(user,date, reviews, star_score, likes, dislikes))

        for n in range(len(data)):
            self.item.add_value('user', data[n][0])
            self.item.add_value('date', data[n][1])
            self.item.add_value('reviews', data[n][2])
            self.item.add_value('star_score', data[n][3])
            self.item.add_value('likes', data[n][4])
            self.item.add_value('dislikes', data[n][5])

        yield self.item.load_item()
