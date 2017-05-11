from __future__ import print_function
import mechanize
import bs4 as bs
import urllib2
import codecs
import sys

import requests

from module import WebCrawler
reload(sys)
sys.setdefaultencoding('utf-8')
letter4 = []
connect = requests.get('https://shop.whois.com/domain-registration/index.php?domain_names=abc.com')
if connect:
    content = connect.text
    bs = bs(content, 'html.parser')
    res_av = bs.find("span", class_="dca-red-text")
print (res_av)

