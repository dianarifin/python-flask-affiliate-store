from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import flask_wtf



@app.route('/')
def callProductTemplate(prodArry):
    return render_template('common-product.html', prods=prodArry)

def callNavTemplate():
    pass

def callFooterTemplate():
    pass


def callSearchTemplate():
    pass



@app.route('/')
def index():
    x = "<a href=\"http://127.0.0.1:5000/hello\"> hello page<a>"
    return x + 'Index Page'

@app.route('/hello')
def hello():
    
    return '<h1>Hello, World   sir</h1>'
@app.route('/checkit', methods=[ 'POST', 'GET'])
def mytest(prods):
    
    return render_template('checkit.html', prods=prods)

@app.route('/mytest', methods=[ 'POST', 'GET'])
def mytest(name=None):
    
    return render_template('mytest.html', name=name)

	
	
@app.route('/mytestvalues', methods=[ 'POST'])
def mytestvalues():
    first = request.form["first_name"] 
    last = request.form["last_name"]
    return render_template('mytestvalues.html',  first=first, last=last)

	
	
	
	
	
