'''
Author : Vipul Sharma
This is script is basically the script of a spider which will crawl to the links as given in the start_urls driven by the conditions implied by
RegEx 
:NOTE: Run the MongoDB instance on the default host and port before running the crawling script by
        sudo service mongodb start 
* Change database name or collection name if necessary.. or add or remove links in start_urls
* Run the crawler by : 
        scrapy crawl crawler_bloom
                or by
        scrapy crawl crawler_bloom -o scraped.json -t json
        (use this to get the json file of scraped articles, this json file wil be created in the current directory)
* The crawler will now perform the required task
* Use pymongo distribution for accessing the extracted articles and their information stored in MongoDB 
'''
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item, Field
from scrapy.spider import BaseSpider
import pymongo
from pymongo import Connection, MongoClient
from bs4 import BeautifulSoup
client = MongoClient()
db = client.test_database                 # database name : change database name client.<db_name>
collection = db.test_collection           # collection name : change collection name db.<collection_name>
class logItem(Item):
    description = Field()
class ExampleSpider(CrawlSpider):
    name = "crawler_bloom"
    allowed_domains = ["bloomberg.com"]
    start_urls = ["http://www.bloomberg.com/news","http://www.bloomberg.com/quickview/","http://www.bloomberg.com/technology/","http://www.bloomberg.com/view/"]
    rules = [Rule(SgmlLinkExtractor(allow=("http://www.bloomberg.com/.*(\.html)$")), callback='parse_item', follow=True),]
    def parse_item(self,response):
        b = logItem()
        a = response.body
        print "\n"*10
        fragment = BeautifulSoup(a)
        ans = fragment.find('div', {'itemprop': 'articleBody'},'h2')
        invalid_tags = ['b', 'i', 'u', 'div', 'figure', 'a', 'html', 'body', 'p', 'h1', 'h2', 'span', 'img', 'strong', 'li', 'ul', 'figcaption', 'br']
        soup = BeautifulSoup(str(ans))
        for tag in invalid_tags: 
            for match in soup.findAll(tag):
                match.replaceWithChildren()
        x2 = bytes(soup).decode('unicode-escape').encode('ascii','ignore')
        x3 = x2.translate(None, '\n')
        b['description'] = x3
        post = {'description':x3}      
        posts = db.posts
        post_id = posts.insert(post)
        return b 

