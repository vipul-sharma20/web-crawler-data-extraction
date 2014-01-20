web-crawler-data-extraction
===========================

A web crawler made in python using Scrapy framework which crawls www.bloomberg.com and scrapes all the articles of the website

What it does:
=============
* The web-crawler crawls all the links of www.bloomberg.com and extracts all the articles and save them as plain text into mongodb or a json file (as specified on running the script)

Requirement:
============

* python v2.7.4
* MongoDB v2.4.9
* Pymongo
* BeautifulSoup(bs4)

How to run:
===========
*Install Python v2.7.4, MongoDB v2.4.9, Pymongo and BeautifulSoup(bs4)

*Firstly, run the MongoDB instance on the default host and port so that PyMongo can create a client for the running MongoDB:
      sudo service mongodb start
*The web-crawler is in /tuto/tuto/spiders as testing.py and the name of our spider is "crawler_bloom" so change directory to  /tuto/tuto/spiders

*In testing.py change the default database name and collection name if necessary. The default name for database is "test_database" and for collection is "test_collection"

*Run the web-crawler in /tuto/tuto/spiders/ by :
    scrapy crawl crawler_bloom
                or by
    scrapy crawl crawler_bloom -o scraped.json -t json
(use this to get the json file of scraped articles. This json file wil be created in the current directory)

*Now, our spider will crawl all the links and will store all the articles extracted from the pages in the MongoDB. The extracted data is also displayed on the terminal screen. A separate scraped.json file of the extracted articles can also be created if second method is used for running the web-crawler
