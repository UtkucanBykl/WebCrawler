import module
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
kelime=raw_input("Aranan Kelime :")
URL = "http://www.tdk.gov.tr/index.php?option=com_gts&view=gts"
b=module.WebCrawlerSearch(URL,"kelime",kelime)
print (module.Crawle(b,"table","hor-minimalist-a"))
print (module.FindLinks(URL))



