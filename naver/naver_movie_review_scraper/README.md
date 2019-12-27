## Naver Movie Review (네이버 영화 평점) Scraper

This code uses this [url](https://movie.naver.com/movie/bi/mi/basic.nhn?code=136873), which is a Frozen2 Naver Movie Review, as an example.</br>
Specifically, this code crawls _movie reviews by audience_ (네티즌 한줄평).


**Overview**:
- `Python Module` used: scrapy (https://scrapy.org/)
- Crawled data (korean):
    * username: username of the reviewer
    * date: date the review was published
    * star_score: score out of 10
    * likes: number of likes the review received
    * dislikes: number of dislikes the review received




**Code**

- running the spider:
  1. open the terminal and `cd` into `naver_movie_scraper/naver_movie/spiders` directory
  2. run `scrapy runspider review_spider.py` in the terminal
  3. Output: json type data

- changing the setting of spider (switching movie):
  1. open `review_spider.py` in `naver_movie_scraper/naver_movie/spiders` directory
  2. Change the `max_page` and `movie_code` variable to the movie you want to scrape
       -  `movie_code`: can be found at the end of the movie review url (e.g. https://movie.naver.com/movie/bi/mi/basic.nhn?code=136873; the movie code is 136873)
       -  `total_review`: number of total reviews (can be found on the movie url under 평점)

- saving the crawled output to csv file:
  1. open the terminal and `cd` into `naver_movie_scraper/naver_movie/spiders` directory
  2. run `scrapy runspider review_spider.py -o <name_of_file>.csv`

<br>
<br>
updated: Dec 20, 2019
