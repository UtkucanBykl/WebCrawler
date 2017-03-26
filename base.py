#!/usr/bin/env python
# -*- coding: utf-8 -*-
import module
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
kelime=raw_input("Aranan Kelime :")
URL = "http://www.tdk.gov.tr/index.php?option=com_gts&view=gts"
b=module.WebCrawlerSearch(URL,"kelime",kelime)
print (module.CrawleWithId(b,"table","hor-minimalist-a"))
print (module.FindLinks("http://stackoverflow.com/questions/6289474/working-with-utf-8-encoding-in-python-source"))
