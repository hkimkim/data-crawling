# Data Crawling

Data Crawling contains three web crawlers that scrapes:

1) user comments on [Daum News articles](https://media.daum.net/) </br>
2) user comments on [Naver News articles](https://news.naver.com/) </br>
3) user reviews on [Naver Movie Review](https://movie.naver.com)

_*Daum and Naver are Korean search engines and web portals_

It uses python `BeutifulSoup` and `scrapy` framework.

## Requirements

* Python 3.6 +
* [scrapy](https://scrapy.org/)
* [BeutifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Directory
* [data_crawling](https://github.com/hkimkim/data_crawling):  root directory
    * [daum](https://github.com/hkimkim/data_crawling/tree/master/daum/)/ contains code for crawling user comments on daum news article </br>
        * [daum_news_scraper]()
    * [naver](https://github.com/hkimkim/data_crawling/tree/master/naver)/ contains code for crawling naver news and naver movie review
        * [naver_movie_review_scraper](https://github.com/hkimkim/data_crawling/tree/master/naver/naver_movie_review_scraper)/ contains code for naver movie review
        * [naver_news_scraper](https://github.com/hkimkim/data_crawling/tree/master/naver/naver_news_scraper)/ contains code for crawling naver news

*_For more details on how to run each scraper, read the README.md in each directory_
