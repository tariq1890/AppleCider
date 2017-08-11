from unittest import TestCase
from TooEarlyForAppleCider.DataAnalyzer import DataAnalyzer


class TestDataAnalyzer(TestCase):
    def test_constructor_works(self):
        analyzer = DataAnalyzer()
        self.assertEqual(analyzer.query_count, 0)
        self.assertEqual(analyzer.stack_overflow, 0)
        self.assertEqual(analyzer.github, 0)
        self.assertEqual(analyzer.everything_else, 0)
