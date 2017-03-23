from __future__ import print_function

import re

import mechanize
import bs4 as bs
import urllib2
import codecs
import sys
import pandas as pd
reload(sys)
sys.setdefaultencoding('utf-8')
kelime=raw_input("Aranan Kelime :")
URL = "http://www.tdk.gov.tr/index.php?option=com_gts&view=gts"
b= mechanize.Browser()
b.set_handle_refresh(False)
b.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]

b.open(URL, timeout=2.0)
b.select_form(nr=0)
b.form["kelime"]=kelime
b.method="post"
response=b.submit()

soup=bs.BeautifulSoup(response.read(),"lxml")
for table in soup.find_all("table",id=re.compile("^hor-minimalist-a$")):
    print (table.text)

