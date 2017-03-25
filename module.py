import re
import bs4 as bs
import mechanize
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def FindLinks(URL):
    b = mechanize.Browser()
    b.set_handle_refresh(False)
    b.addheaders = [('User-agent',
                     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]

    b.open(URL, timeout=2.0)
    links=[]
    for link in b.links():
        links.append(link.text)
    return links

def WebCrawlerSearch(URL,inputName,search):
    b=mechanize.Browser()
    b.set_handle_refresh(False)
    b.addheaders = [('User-agent',
                     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]

    b.open(URL, timeout=2.0)
    b.select_form(nr=0)
    b.form[inputName] = search
    b.method = "post"
    response = b.submit()
    return response

def Crawle(response,tag,id):
    find=[]
    soup = bs.BeautifulSoup(response.read(), "lxml")
    for search in soup.find_all(tag, id=re.compile("^"+id+"$")):
        find.append(search.text)
    if not find:
        return "No Match"
    else:
        return find
