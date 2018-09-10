import feedparser
import flask, requests



def buyLinkBuilder(baseUrl, refId):
    return baseUrl  + refId

def linkBuilder(baseUrl, product, refId):
    return baseUrl + product + refId

def getProdId(url):
    # get product id 
    prodId =url.split('-')
    return prodId[1]

def buildRssLink(baseUrl, searchQuery):
    return baseUrl + searchQuery

def getFeed(url):
    data = feedparser.parse(url)

def getCode():
    pass

def myProducts(feed):
    arry= []
    for i in d.entries:
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


def runApp():
	pass
