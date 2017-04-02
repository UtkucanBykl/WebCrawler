#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import bs4 as bs
import mechanize
import sys
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')

def FindLinks(URL):
    b = mechanize.Browser()
    b.set_handle_refresh(False)
    b.set_handle_robots(False)
    b.addheaders = [('User-agent',
                     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
    try:
        b.open(URL, timeout=2.0)
    except:
        return "<h1>Error</h1>"
    links=[]
    for link in b.links():

        links.append(str(link.text)+"-"+str(link.url))

    if not links:
        return "No found link"
    else:
        return links

def WebCrawlerSearch(URL,inputName,search):
    b=mechanize.Browser()
    b.set_handle_refresh(False)
    b.set_handle_robots(False)
    b.addheaders = [('User-agent',
                     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
    try:
        b.open(URL, timeout=2.0)
    except:
        return "<h1>Error</h1>"
    b.select_form(nr=0)
    b.form[inputName] = search
    b.method = "post"
    response = b.submit()
    return response

def CrawleWithId(response,tag,id):
    find=[]
    response=urllib2.urlopen(response).read()
    soup = bs.BeautifulSoup(response, "lxml")
    for search in soup.find_all(tag, id=re.compile("^"+id+"$")):
        find.append(search.text)
    if not find:
        return "No Match"
    else:
        return find

def CrawleWithClass(response,tag,class_):
    find = []
<<<<<<< HEAD
    try:
        response=urllib2.urlopen(response).read()
        soup = bs.BeautifulSoup(response, "lxml")
    except:
        return "Error"
=======
    response=urllib2.urlopen(response).read()
    soup = bs.BeautifulSoup(response, "lxml")
>>>>>>> 141cadcc69b16ad8e24b77e1e82a9349ffb962d7
    for search in soup.find_all(tag,class_=class_):
        find.append(search.text)
    if not find:
        return "No Match"
    else:
        return find
