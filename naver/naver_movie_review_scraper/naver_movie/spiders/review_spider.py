import scrapy
from scrapy.http import Request
import math



class ReviewSpider(scrapy.Spider):
    name = "movie_spider"
    total_reviews = 19945
    movie_code = 136873 #겨울왕국2

    def start_requests(self):
        for i in range(1, math.ceil(self.total_reviews/10)):
            yield Request('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={0}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={1}'.format(self.movie_code, i))

    def parse(self, response):
        user = response.css('div.score_reple dt em a span::text').extract()
        date = response.css('div.score_reple dt em:last-child::text').extract()
        reviews = [response.css('div.score_reple p span#_filtered_ment_'+str(n)+"::text").extract() for n in range(10) ]
        star_score = response.css('div.star_score em::text').extract()
        likes = response.css('a._sympathyButton strong::text').extract()
        dislikes = response.css('a._notSympathyButton strong::text').extract()

        data = list(zip(user,date, reviews, star_score, likes, dislikes))

        for n in range(len(data)):
            yield {
                'user': user[n],
                'date': date[n],
                'score': star_score[n],
                'review': reviews[n][0].strip(),
                'likes' : likes[n],
                'dislikes': dislikes[n]
            }
