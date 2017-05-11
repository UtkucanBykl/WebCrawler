#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
from module import WebCrawler
from mongodb import MongoDB
app = Flask(__name__)
WebCrawler = WebCrawler()
Mongo=MongoDB()

@app.route("/")
def index():
    response=Mongo.UrlListDate()
    return render_template("index.html",response=response)

@app.route("/findlinks")
def FindLinks():
    return render_template("findlink.html")

@app.route('/find', methods=['POST'])
def form_post():
    URL=request.form["url"]
    Mongo.UrlSearch(URL)
    b=WebCrawler.FindLinks(URL)
    return render_template("linkans.html",response=b,url=URL);

@app.route("/crawle")
def Crawle():
    return render_template("findtag.html")

@app.route('/crawle', methods=['POST'])
def form_postt():
    URL=request.form["url"]
    tag=request.form["tag"]
    class_=request.form["class"]
    Mongo.UrlSearch(URL)
    return render_template('findcrawle.html', response=WebCrawler.CrawleWithClass(URL,tag,class_),tag=tag,class_=class_)

@app.route('/howmany')
def HowMany():
    response=Mongo.UrlListCount()
    return render_template("howmany.html",response=response)



if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=12345, use_reloader=True)
