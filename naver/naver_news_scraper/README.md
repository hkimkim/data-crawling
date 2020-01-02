# Naver News Scraper

>Naver News Scraper is a web crawler that scrapes user comments from Naver news articles.

Naver News Scraper is useful to those trying to scrape user comments from Naver news articles. It uses python `scrapy` framework.

[Naver](www.naver.com) is a Korean web portal.

## Requirements

* Python 3.6 +
* [scrapy](https://scrapy.org/)


## Directory Structure
* [naver_news_scraper/naver_news](https://github.com/hkimkim/data_crawling/tree/master/naver/naver_news_scraper/naver_news):  root directory
  * [spiders](https://github.com/hkimkim/data_crawling/tree/master/naver/naver_news_scraper/naver_news/spiders)/ contains the web crawler/spider for scraping
    * [news_comment_spider.py](https://github.com/hkimkim/data_crawling/blob/master/naver/naver_news_scraper/naver_news/spiders/news_comment_spider.py)/ python code of the data crawling spider
  * [items.py](https://github.com/hkimkim/data_crawling/blob/master/naver/naver_news_scraper/naver_news/items.py)/ default scrapy python script that defines how and where to store scraped data
  * [middlewares.py](https://github.com/hkimkim/data_crawling/blob/master/naver/naver_news_scraper/naver_news/middlewares.py)/default scrapy python script that customizes plugs that process the responses
  * [pipelines.py](https://github.com/hkimkim/data_crawling/blob/master/naver/naver_news_scraper/naver_news/pipelines.py)/ default scrapy python script that processes the scraped data into desired format
  * [settings.py](https://github.com/hkimkim/data_crawling/blob/master/naver/naver_news_scraper/naver_news/settings.py)/ default scrapy python script that defines the data crawling spider's settings


**For more detailed guide of `scrapy` refer to https://docs.scrapy.org/en/latest/index.html*

## Running the Spider
1. Fork the repository.

2. Clone your forked repository to your machine.</br>
  <code> git clone https://github.com/hkimkim/data_crawling.git</code>


3. Navigate into `/spiders` directory</br>
`cd /<your machine directory>/data_crawling/naver/naver_news_scraper/naver_news/spiders`.

4. Open `naver_news_scraper.py` and copy and paste the link of the naver news article you want to crawl into the `url` variable on line 13.

5. Run <code> scrapy runspider naver_news_scraper.py </code> </br>
![Alt Text](https://media.giphy.com/media/U3VVbR1DMej8GZXJl8/giphy.gif)
6. To save the crawled outcome to a .csv file, run the code:</br> `scrapy runspider naver_news_scraper.py -o <name_of_file>.csv`
