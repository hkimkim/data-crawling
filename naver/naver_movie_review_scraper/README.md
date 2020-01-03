# Naver Movie Review Scraper (네이버 영화 평점)

Naver Movie Review Scraper is a web crawler that scrapes user movie reviews(네티즌 한줄평) from [Naver Movie Review](https://movie.naver.com).

Naver News Scraper is useful to those trying to scrape user movie reviews from Naver Movie Review. It uses python `scrapy` framework.

## Requirements

* Python 3.6 +
* [scrapy](https://scrapy.org/)


## Directory Structure
* [naver_movie](https://github.com/hkimkim/data_crawling/tree/master/naver/naver_movie_review_scraper/naver_movie):  root directory
  * [spiders](https://github.com/hkimkim/data_crawling/tree/master/naver/naver_movie_review_scraper/naver_movie/spiders)/ contains the web crawlers/spiders for scraping
    * [merged_spider.py](https://github.com/hkimkim/data_crawling/blob/master/naver/naver_movie_review_scraper/naver_movie/spiders/merged_spider.py)/ contains code for spider that crawls all the user reviews from [top 40 best movies](https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200102)
    * [review_spider.py](https://github.com/hkimkim/data_crawling/blob/master/naver/naver_movie_review_scraper/naver_movie/spiders/review_spider.py)/contains code for spider that crawls user reviews from one specified movie
  * [items.py](https://github.com/hkimkim/data_crawling/blob/master/naver/naver_news_scraper/naver_news//items.py)/ default scrapy python script that defines how and where to store scraped data
  * [middlewares.py](https://github.com/hkimkim/data_crawling/blob/master/naver/naver_news_scraper/naver_news/middlewares.py)/default scrapy python script that customizes plugs that process the responses
  * [pipelines.py](https://github.com/hkimkim/data_crawling/blob/master/naver/naver_news_scraper/naver_news/pipelines.py)/ default scrapy python script that processes the scraped data into desired format
  * [settings.py](https://github.com/hkimkim/data_crawling/blob/master/naver/naver_news_scraper/naver_news/settings.py)/ default scrapy python script that defines the data crawling spider's settings


**For more detailed guide of `scrapy` refer to https://docs.scrapy.org/en/latest/index.html*

## Running the Spiders

### 1) review_spider

> `review_spider` is a spider that crawls user reviews of one movie review. For example, the code crawls [Frozen 2 Movie Review](https://movie.naver.com/movie/bi/mi/basic.nhn?code=136873).

1. Fork the repository.

2. Clone your forked repository to your machine.</br>
``` git clone https://github.com/hkimkim/data_crawling.git ```

3. Navigate into `/spiders` directory</br>
`cd /<your machine directory>/data_crawling/naver/naver_movie_review_scraper/naver_movie/spiders`.

4. Open `review_spider.py` and copy and paste the link of the movie you want to crawl into the `url` variable on line 14.
![Imgur](https://i.imgur.com/mSvQJDs.png)


5. Run <code> scrapy runspider review_spider.py </code> </br>
![Alt Text](https://media.giphy.com/media/iEvzrMb842gYMykC4L/giphy.gif)

6. To save the crawled outcome to a .csv file, run the code:</br> `scrapy runspider review_spider.py -o <name_of_file>.csv`

#### Scraped Data Features:
-   username: username of the reviewer
-   date: date the review was made
-   star_score: score out of 10
-   likes: number of likes the review received
-   dislikes: number of dislikes the review received
-   reviews: review written by the user

</br>

### 2) merged_spider

> `merged_spider` is a spider that crawls all the user reviews from [top 40 best movies](https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200102) from today's date standard.

1. Fork the repository.

2. Clone your forked repository to your machine.</br>
``` git clone https://github.com/hkimkim/data_crawling.git ```

3. Navigate into `/spiders` directory</br>
`cd /<your machine directory>/data_crawling/naver/naver_movie_review_scraper/naver_movie/spiders`.

4. Run <code> scrapy runspider merged_spider.py </code> </br>
![Alt Text](https://media.giphy.com/media/dxHtppiLTg5ySCJdDq/giphy.gif)

6. To save the crawled outcome to a .csv file, run the code:</br> `scrapy runspider merged_spider.py -o <name_of_file>.csv`

#### Scraped Data Features:
-   title: title of the movie crawled
-   username: username of the reviewer
-   date: date the review was made
-   star_score: score out of 10
-   likes: number of likes the review received
-   dislikes: number of dislikes the review received
-   reviews: review written by the user

***
