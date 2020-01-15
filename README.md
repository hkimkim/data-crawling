# Data Scraping

Data Scraping contains three web crawlers that scrapes:

1) user comments on [Daum News articles](https://media.daum.net/) </br>
2) user comments on [Naver News articles](https://news.naver.com/) </br>
3) user reviews on [Naver Movie Review](https://movie.naver.com)

_*Daum and Naver are Korean search engines and web portals_

It uses `scrapy` framework and python `json` module to scrape and parse the scraped data.

## Requirements

* Python 3.6 +
* [scrapy](https://scrapy.org/)
* [jupyter notebook](https://jupyter.org/install)


## Directory
* [data_scraping](https://github.com/hkimkim/data_scraping):  root directory
    * [daum](https://github.com/hkimkim/data_scraping/tree/master/daum/)/ contains code for scraping user comments on daum news article </br>
    * [naver](https://github.com/hkimkim/data_scraping/tree/master/naver)/ contains code for scraping naver news and naver movie review
        * [naver_movie_review_scraper](https://github.com/hkimkim/data_scraping/tree/master/naver/naver_movie_review_scraper)/ contains code for naver movie review
        * [naver_news_scraper](https://github.com/hkimkim/data_scraping/tree/master/naver/naver_news_scraper)/ contains code for scraping naver news

*_For more details on how to run each scraper, read the README.md in each directory_
