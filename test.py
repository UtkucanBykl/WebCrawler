import unittest
from module import WebCrawler

class Test(unittest.TestCase):


    def test_crawle(self):
        b=WebCrawler("www.utkucanbiyikli.me")
        self.assertNotEqual(b.FindLinks("www.utkucanbiyikli.me"),"Error")

    def test_in(self):
        self.assertIn("Hello","Hello")
    def test_out(self):
	self.assertIn("adasdas","asdas")
