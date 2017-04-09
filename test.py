import unittest
import module

class Test(unittest.TestCase):


    def test_crawle(self):
        a=str(module.CrawleWithClass("www.facebook.com","divdad","grdasdaadient"))
        self.assertIsNotNone(a)

