#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import module
app = Flask(__name__)


@app.route("/")
def index():
    return "Utkucan Bıyıklı"

@app.route("/findlinks")
def FindLinks():
    return render_template("findlink.html")

@app.route('/find', methods=['POST'])
def form_post():
    URL=request.form["url"]
    b=module.FindLinks(URL)
    return str(b)

@app.route("/crawle")
def Crawle():
    return render_template("findtag.html")

@app.route('/crawle', methods=['POST'])
def form_postt():
    URL=request.form["url"]
    tag=request.form["tag"]
    class_=request.form["id"]
    return str(module.CrawleWithClass(URL,tag,class_))



if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=12345, use_reloader=True)
