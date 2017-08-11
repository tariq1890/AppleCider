from unittest import TestCase
from TooEarlyForAppleCider.SoupyCrawler import SoupyCrawler


class TestSoupyCrawler(TestCase):
    def test_crawler_has_209_stopwords(self):
        crawler = SoupyCrawler()
        self.assertEqual(len(crawler.stop_words), 209)
