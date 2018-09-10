import feedparser
import flask
import sqlite3
import random

def getFeed(url):
    return feedparser.parse(url)

def myProducts(feed):
    arry= []
    for i in feed.entries:
        i = i
        title = i.title
        largeImage = i.media_content[0]['url']
        bl = i.link
        buyLink =  buyLinkBuilder(bl,refID )
        price = i.price
        author = i.author
        prodId =getProdId(bl)
        relatedProdsLink =linkBuilder(baseRelatedItemsLink, prodId ,refID )
        arry.append([title, largeImage, buyLink, price, author, relatedProdsLink])
    return arry


def org_myProducts(feed):
    arry= []
    for i in feed.entries:
        i = i
        title = i.title
        largeImage = i.media_content[0]['url']
        bl = i.link
        buyLink =  buyLinkBuilder(bl,refID )
        price = i.price
        author = i.author
        prodId =getProdId(bl)
        relatedProdsLink =linkBuilder(baseRelatedItemsLink, prodId ,refID )
        arry.append((title, largeImage, buyLink, price, author, relatedProdsLink ))
    return arry

def getRandomProd(prods):
    return   random.randint(0, len(prods))

###
###todo or not currently using and delete
###  
def getCode():
    pass

def buyLinkBuilder(baseUrl, refId):
    return baseUrl  + refId

def linkBuilder(baseUrl, product, refId):
    return baseUrl + product + refId

def getProdId(url):
    # get product id 
    prodId =url.split('-')
    return prodId[1]

def getSearch(search):
    pass


# to do db and search


baseFeed ='http://feed.zazzle.com/tjk_creative/rss'
test01 =  'http://feed.zazzle.com/rss?qs=tshirts&st=popularity&sp=30&ps=100&at238767197743441767'
url2 = "http://feed.zazzle.com/tjk_creative/rss?qs=tshirts&st=popularity&sp=30&ps=100&at238767197743441767"
#link to design on other produts
baseRelatedItemsLink = 'http://www.zazzle.com/s/gifts?gp='
refID= "&rf=238767197743441767&tc=flsk"



url = 'http://feed.zazzle.com/tjk_creative/rss?qs=tshirts'

myfeed = getFeed(url)
mprods =myProducts(myfeed)



"""
#rss stuff
qs=tshirts&st=popularity&sp=30

tshirts?ps=120&fet=162858707277173769


baseTshirtURL ="https://feed.zazzle.com/rss?qs=tshirts"
search = search
popularity = "&st=popularity&sp=120"
page = 1
page += 1


https://feed.zazzle.com/rss?qs=tshirts&st=popularity&sp=60

raglin
mens
womens
kids
baby
Disney
dc comics
batman
scooby doo
harry potter
funny
nerd
politics
pop culture
raglin

"""










