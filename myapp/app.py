from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import flask_wtf
import forms, models, views

#cd C:\Users\Kleszczewski  tim\Desktop\zazzle-store-flask\myapp
#set FLASK_APP=app.py
#python -m flask run


app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True







baseFeed ='http://feed.zazzle.com/tjk_creative/rss'
test01 =  'http://feed.zazzle.com/rss?qs=tshirts&st=popularity&sp=30&ps=100&at238767197743441767'
url2 = "http://feed.zazzle.com/tjk_creative/rss?qs=tshirts&st=popularity&sp=30&ps=100&at238767197743441767"
#link to design on other produts
baseRelatedItemsLink = 'http://www.zazzle.com/s/gifts?gp='
refID= "&rf=238767197743441767&tc=flsk"



if __name__=="__main__":
    app.run(debug=True)











    
