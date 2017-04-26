#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
from module import WebCrawler
app = Flask(__name__)


@app.route("/")
def index():
    return "Utkucan Bıyıklı"

@app.route("/findlinks")
def FindLinks():
    return render_template("findlink.html")

@app.route('/find', methods=['POST'])
def form_post():
    a=WebCrawler()
    URL=request.form["url"]
    b=a.FindLinks(URL)
    return render_template("linkans.html",response=b);

@app.route("/crawle")
def Crawle():
    return render_template("findtag.html")

@app.route('/crawle', methods=['POST'])
def form_postt():
    URL=request.form["url"]
    tag=request.form["tag"]
    class_=request.form["class"]
    a=WebCrawler()
    return render_template('findcrawle.html', response=a.CrawleWithClass(URL,tag,class_))




if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=False, port=12345, use_reloader=True)
