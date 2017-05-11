from datetime import datetime

import pymongo
from pymongo import MongoClient


class MongoDB():


    def __init__(self):

        self.client = MongoClient()

        self.db = self.client["wwebcrawler"]

        self.collection = self.db["wwebcrawlercollection"]



    def Insert(self,url,count):

        urll={

            "url":url,

            "count":count,

            "date":datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        }

        try:

            self.collection.insert(urll)


        except:

            return False


    def UrlList(self):

        myresults = list(self.collection.find().sort("count",pymongo.DESCENDING))[:10]

        return myresults


    def UrlSearch(self,url):
        result=self.collection.find_one({"url":url})
        count=0
        if(not result):
            self.Insert(url,count+1)
        else:
            count=result["count"]+1
            self.collection.update({"url":url},
                                   {
            "$set":{
                "url":url,
                "count":count,
                "date": datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            }
            }
            )
