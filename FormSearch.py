from __future__ import print_function
import mechanize
import bs4 as bs
import urllib2
import codecs
import sys
from module import WebCrawler
reload(sys)
sys.setdefaultencoding('utf-8')
b=WebCrawler()
a=b.CrawleWithClass("https://www.tutorialspoint.com/python/python_classes_objects.htm","pre","")
print(a)


