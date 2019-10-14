import unittest
from app.models import news_Article
class Test__news_Article(unittest.TestCase):
    
    def setUp(self):
        self.new_article = news_Article(1,'The numbers are going up but not very much','Fox News Today','https://www.cnbc.com/2019/07/26/us-gdp-second-quarter-2019.html','Growth decelerated in the second quarter but not by as much as Wall Street thought')


