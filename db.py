#!/usr/bin/python
import sqlite3
class Database():
    def __init__(self):
        self
    def Connect(self):
        conn = sqlite3.connect('webcrawler.db')
        return conn
    def CreateTable(self):
        conn=self.Connect()
        try:
            conn.execute('''CREATE TABLE SEARCH
                   (ID INT PRIMARY KEY     NOT NULL,
                    URL           TEXT    NOT NULL,
                    DATE            DATE     NOT NULL);''')
            return True
        except SystemError,e:
            return e
    def Insert(self,url,date):
        conn=self.Connect()
        conn.execute("INSERT INTO SEARCH (ID,URL,DATE) \
              VALUES (13,"+url+","+date+")");


        conn.commit()
        conn.close()

    def Show(self):
        conn=self.Connect()
        cursor = conn.execute("SELECT id, url, date  from SEARCH")
        for row in cursor:
            print "ID = ", row[0]
            print "URL = ", row[1]
        conn.close()
a=Database()
a.Insert("utku","10")
a.Show()
