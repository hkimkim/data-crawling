# Daum News Scraper

Daum News Scraper is a web scraper that scrapes user comments from [Daum news](https://media.daum.net/).

Daum News Scraper is useful to those trying to scrape user comments from Daum News. It crawls API of the daum news article, which scrapes a json file, and is then parsed using python `json` module.

## Requirements
* Python 3.6 +
* [jupyter notebook](https://jupyter.org/install)

## Modules Used
* requests
* json

## Running the code

1. Open web developer tool of the article link you are trying to scrape.

2. Go into **Network > XHR** and click the file that starts with `comments?...`. Then click `Preview` and you will see `postId`.

  ![Imgur](https://i.imgur.com/lWpyxWH.png)

3. Run `daum_news_comment_scraper.ipynb` on jupyter notebook

4. Copy and paste `postId` into the `postId` variable of the jupyter notebook.

  ![Imgur](https://i.imgur.com/s28gQ9N.png)

5. Run the remaining code.



### _Daum News Article API structure_

- basic API URL Format: http://comment.daum.net/apis/v1/posts/{post_id}/comments?parentId=0&offset={id_of_comment}&limit={number_of_comments_to_call_from_API}&sort=RECOMMEND


- Elements of the URL:
    * **post_id**: post id in API
      - Finding the post_id of news article (Chrome):
        * Open developer tool in Chrome
        * Go into network > XHR > select the url that starts with "comments?"
        * You can find postid in Preview

    * **offset**: id of the comment (in order starting from 0)
    * **limit**: number of comments to call from api


## Scraped Data Features:
-   title: title of the article
-   publishedDate: date the article was published
-   id: Id of the each comment instance
-   userId: Id number of the user
-   postId: Id of the comment post
-   content: comment by the user
-   createdAt: date the comment was posted
-   updatedAt: date the comment was updated
-   childCount: number of replies to the comment
-   likeCount: number of likes the comment received
-   dislikeCount: number of dislikes the comment received
-   recommendCount: number of likes - number of dislikes
-   username: Daum user id
-   displayName: display name of the user (a.k.a Daum nickname)
-   commentCount: total number of comments the user has written on Daum
