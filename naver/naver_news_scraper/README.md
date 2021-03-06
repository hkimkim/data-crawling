# Naver News Scraper

Naver News Scraper is a web scraper that scrapes user comments from Naver news articles.

Naver News Scraper is useful to those trying to scrape user comments from Naver news articles. It uses python `scrapy` framework.

**[Naver](www.naver.com) is a Korean web portal.*

## Requirements

* Python 3.6 +
* [scrapy](https://scrapy.org/)


## Directory Structure
* [naver_news_scraper/naver_news](https://github.com/hkimkim/data-crawling/tree/master/naver/naver_news_scraper/naver_news):  root directory
  * [spiders](https://github.com/hkimkim/data-crawling/tree/master/naver/naver_news_scraper/naver_news/spiders)/ contains the web scraper/spider for scraping
    * [news_comment_spider.py](https://github.com/hkimkim/data-crawling/blob/master/naver/naver_news_scraper/naver_news/spiders/news_comment_spider.py)/ python code of the data scraping spider
  * [items.py](https://github.com/hkimkim/data-crawling/blob/master/naver/naver_news_scraper/naver_news/items.py)/ default scrapy python script that defines how and where to store scraped data
  * [middlewares.py](https://github.com/hkimkim/data-crawling/blob/master/naver/naver_news_scraper/naver_news/middlewares.py)/default scrapy python script that customizes plugs that process the responses
  * [pipelines.py](https://github.com/hkimkim/data-crawling/blob/master/naver/naver_news_scraper/naver_news/pipelines.py)/ default scrapy python script that processes the scraped data into desired format
  * [settings.py](https://github.com/hkimkim/data-crawling/blob/master/naver/naver_news_scraper/naver_news/settings.py)/ default scrapy python script that defines the data scraping spider's settings


**For more detailed guide of `scrapy` refer to https://docs.scrapy.org/en/latest/index.html*

## Running the Spider
1. Fork the repository.

2. Clone your forked repository to your machine.</br>
``` git clone https://github.com/hkimkim/data-crawling.git ```


3. Navigate into `/spiders` directory</br>
`cd /<your machine directory>/data-crawling/naver/naver_news_scraper/naver_news/spiders`.

4. Open `naver_news_scraper.py` and copy and paste the link of the naver news article you want to scrape into the `url` variable on line 13.
![Imgur](https://i.imgur.com/llM8NvZ.png?1)


5. Run <code> scrapy runspider naver_news_scraper.py</code> in terminal. </br>
![Alt Text](https://media.giphy.com/media/U3VVbR1DMej8GZXJl8/giphy.gif)

6. To save the scraped outcome to a .csv file, run the code:</br> `scrapy runspider naver_news_scraper.py -o <name_of_file>.csv`

## Scraped Data Features:
-   userName: user ID of commenter
-   date: date the comment was posted
-   title: title of the news article
-   press: name of press of the news article
-   content: comment by the user
-   likes: number of likes the comment received
-   dislikes: number of dislikes the comment received
-   sad: number of sad reactions for the article (슬퍼요)
-   like: number of like reactions for the article (좋아요)
-   angry: number of angry reactions for the article (화나요)
-   want: number of want reactions for the article (후속기사 원해요)
-   warm: number of warm reactions for the article (훈훈해요)

***
