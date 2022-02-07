# Data Crawling
[Last Updated Jan 2020]]

I wrote a [blog post](https://hkimkim.github.io/python/scrapy/2020/01/18/data-crawling.html) explaining the concept of web crawling and the pros and cons of the popular web crawling python modules.

Data Crawling contains three web crawlers that crawls:

1) user comments on [Daum News articles](https://media.daum.net/) </br>
2) user comments on [Naver News articles](https://news.naver.com/) </br>
3) user reviews on [Naver Movie Review](https://movie.naver.com)

_*Daum and Naver are Korean search engines and web portals_

It uses `scrapy` framework and python `json` module to crawl and parse the scraped data.

## Requirements

* Python 3.6 +
* [scrapy](https://scrapy.org/)
* [jupyter notebook](https://jupyter.org/install)


## Directory
* [data-crawling](https://github.com/hkimkim/data-crawling):  root directory
    * [daum](https://github.com/hkimkim/data-crawling/tree/master/daum/)/ contains code for scraping user comments on daum news article </br>
    * [naver](https://github.com/hkimkim/data-crawling/tree/master/naver)/ contains code for scraping naver news and naver movie review
        * [naver_movie_review_scraper](https://github.com/hkimkim/data-crawling/tree/master/naver/naver_movie_review_scraper)/ contains code for naver movie review
        * [naver_news_scraper](https://github.com/hkimkim/data-crawling/tree/master/naver/naver_news_scraper)/ contains code for scraping naver news

*_For more details on how to run each scraper, read the README.md in each directory_

