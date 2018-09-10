from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import flask_wtf
import feedparser


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def hello():
    return "Hello World!"




#searchform
#layout
#common-product
#common-nav
#common-footer
#landing-products

##
### http://www.zazzle.com/sell/affiliates/promotionaltools/rss
###
###  http://www.zazzle.com/api
###
###
##


@app.route('/index', methods=[ 'POST', 'GET'])
def index():
    return render_template('layout.html')

@app.route('/mytestvalues2', methods=[ 'POST'])
def mytestvalues2(s):
    #s = request.form["search_test"]     
    return render_template('mytestvalues2.html', mysearch=s)

@app.route('/common-product', methods=[ 'POST'])
def commonProducts():
    url = 'http://feed.zazzle.com/tjk_creative/rss?qs=tshirts%20'
    search = getSearch()
    print(search)
    rssLink = buildRssLink(url, search.replace(" ", "%20"))
    print("got here rssLink:  ",  rssLink)
    f =  getFeed(rssLink)
    print("got here f")
    populateTemplateData =myProducts(f)
    print("got here populateTemplateData")
    
    print("got here prods: ", populateTemplateData[0])
    #s = request.form["search_test"]     
    return render_template('common-product.html', prods=populateTemplateData)

#
# Data manipulations
def getSearch():
    return request.form["search_test"]     


def buyLinkBuilder(baseUrl, refId):
    if "?" in baseUrl:
        return baseUrl  + "&rf" + refId
    else:
        return baseUrl  + "?rf" + refId

def linkBuilder(baseUrl, product, refId):
    return baseUrl + product + refId

def getProdId(url):
    # get product id 
    prodId =url.split('-')
    return prodId[1]

def buildRssLink(baseUrl, searchQuery):
    return baseUrl + searchQuery

def getFeed(url):
    return feedparser.parse(url)

def getCode():
    pass

def myProducts(feed):
    arry= []
    refID = "238767197743441767"
    baseRelatedItemsLink="todoadd"
    for i in feed.entries:
        i = i
        title = i.title
        largeImage = i.media_content[0]['url']
        bl = i.link
        buyLink =  buyLinkBuilder(bl,refID )
        price = i.price
        author = i.author
        prodId =getProdId(bl)
        #
        #
        relatedProdsLink =linkBuilder(baseRelatedItemsLink, prodId ,refID )
        arry.append([title, largeImage, buyLink, price, author, relatedProdsLink])
    return arry



"""
def runMyApp():
	url = 'http://feed.zazzle.com/tjk_creative/rss?qs=tshirts%20'
	search = getSearch()
	rssLink = buildRssLink(url, search)
	f =  getFeed(rssLink)
	populateTemplateData =myProducts(f)
	commonProducts(populateTemplateData)

"""
#todo
#   & or ?
# replace spaces with %20
#get deal
#
#
#
#
#
##
## todo database stuff


"""
@app.route('/index', methods=[ 'POST', 'GET'])
def index():
    return render_template('searchform.html')

@app.route('/mytestvalues2', methods=[ 'POST'])
def mytestvalues2():
    s = request.form["search_test"]     
    return render_template('mytestvalues2.html', mysearch=s)

@app.route('/mytest', methods=[ 'POST', 'GET'])
def mytest():
    return render_template('mytest.html')

@app.route('/mytestvalues', methods=[ 'POST'])
def mytestvalues():
    first = request.form["first_name"] 
    last = request.form["last_name"]
    return render_template('mytestvalues.html',  first=first, last=last)
"""




if __name__=="__main__":
    app.run()
