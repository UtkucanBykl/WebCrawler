#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import bs4 as bs
import mechanize
import sys
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')

class WebCrawler():
    def __init__(self):

        self.b = mechanize.Browser()
        self.b.set_handle_refresh(False)
        self.b.set_handle_robots(False)
        self.b.addheaders = [('User-agent',
                     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]

    def FindLinks(self,URL):

        try:
            self.b.open(URL, timeout=2.0)
        except mechanize.HTTPError,e:
            return e
        links=[]
        for link in self.b.links():

            links.append(str(link.text)+"-"+str(link.url))

        if not links:
            return "No found link"
        else:
            return links

    def WebCrawlerSearch(self,URL,inputName,search):

        try:
            self.b.open(URL, timeout=2.0)
        except mechanize.HTTPError, e:
            return e
        self.b.select_form(nr=0)
        self.b.form[inputName] = search
        self.b.method = "post"
        response = self.b.submit()
        return response

    def CrawleWithId(self,response,tag,id):
        find=[]
        response=urllib2.urlopen(response).read()
        soup = bs.BeautifulSoup(response, "lxml")
        for search in soup.find_all(tag, id=re.compile("^"+id+"$")):
            find.append(search.text)
        if not find:
            return "No Match"
        else:
            return find

    def CrawleWithClass(self,response,tag,class_):
        find = []
        try:
            response=urllib2.urlopen(response).read()
            soup = bs.BeautifulSoup(response, "lxml")
        except mechanize.HTTPError, e:
            return e

        for search in soup.find_all(tag,class_=class_):
            find.append(search.text)
        if not find:
            return "No Match"
        else:
            return find
