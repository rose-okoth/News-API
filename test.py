import unittest
from models import news

News=news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news = News('CNN','CNN','Surviving in a pandemic','Effects of Covid 19 in the past year',2021-2-22,'https://cnn.com','https://image.tmdb.org/t/p/w500/khsjha27hbs')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))


if __name__ == '__main__':
    unittest.main()