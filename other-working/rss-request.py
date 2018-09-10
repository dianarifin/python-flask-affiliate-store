import requests, xml
import jinja2
from bs4 import BeautifulSoup
import feedparser
import flask

##   ass id &rf=238767197743441767



baseFeed ='http://feed.zazzle.com/tjk_creative/rss'
test01 =  'http://feed.zazzle.com/rss?qs=tshirts&st=popularity&sp=30&ps=100&at238767197743441767'
url2 = "http://feed.zazzle.com/tjk_creative/rss?qs=tshirts&st=popularity&sp=30&ps=100&at238767197743441767"

d = feedparser.parse(url2)
#prod.keys()

#print (d['feed']['title'])

d.entries[0]
d.entries[0]
x = d.entries[1]
x.media_keywords
x.title

z = x.media_content[0]
largeThumb = z['url']

####
prod = d.entries[0]

## need from rss feed
title = prod.title
largeImage = prod.media_content[0]['url']
link = prod.link
price = prod.price
author = prod.author
#link to auther store

#link to design on other produts
baseRlatedLink = 'http://www.zazzle.com/s/gifts?gp='

# get product id 
prodId =link.split('-')
prodId = prodId[1]
#add referal id
refID= "&rf=238767197743441767&tc=flsk"

relatedProdsLink = baseRlatedLink + prodId + refID

#promocode




#thumImage = prod.media_thumbnail[0]['url']

for i in d.entries:
    i = i
    pass


#links = prod.links
#rating = prod.rating
#author_detail = prod.author_detail
#published = prod.published
#title = prod.title
#authors = prod.authors
#summary_detail =prod.summary_detail
#media_price = prod.media_price
#media_rating = prod.media_rating
#media_keywords = prod.media_keywords
#tags = prod.tags
#guidislink = prod.guidislink
#media_thumbnail =prod.media_thumbnail
#title_detail = prod.title_detail
#summary =prod.summary
#content = prod.content
#side_ids = prod.id
#author = prod.author
#href = prod.href
#published_parsed = prod.published_parsed
#price = prod.price
#media_content = prod.media_content

















"""


#clean up
desc = prod.media_description


'''
for i in d.entries:
	print(i)
'''


#baseFeed ='http://feed.zazzle.com/tjk_creative/rss'
#query = ""
#size = ""
#product = ""


#r = requests.get(baseFeed)
#r.headers['content-type']
#r.encoding
#r.text


#soup = BeautifulSoup(r.text, "html.parser")



###
"""



"""
d = feedparser.parse(url2)
d.entries[0]
d.entries[0]
x = d.entries[1]
x.media_keywords
x.title

z = x.media_content[0]
largeThumb = z['url']

####
prod = d.entries[0]

## need from rss feed
title = prod.title
largeImage = prod.media_content[0]['url']
link = prod.link
price = prod.price
author = prod.author
#link to auther store


# get product id 
prodId =link.split('-')
prodId = prodId[1]
#add referal id


####relatedProdsLink = baseRlatedLink + prodId + refID

#promocode



#thumImage = prod.media_thumbnail[0]['url']
"""

"""
for i in arry:
    print(arry[0])
    print(arry[1])
    print(arry[2])
    print(arry[3])
    print(arry[4])
    print(arry[5])
"""
"""
for i in d.entries:
    i = i
    title = i.title
    largeImage = i.media_content[0]['url']
    link = i.link
    price = i.price
    author = i.author

    prodId =link.split('-')
    prodId = prodId[1]
    x =linkBuilder(baseRelatedItemsLink, prodId ,refID )
    print(title, largeImage, link, price, author )
    print('this is x: ' , x)
"""
