import ast
from urllib.parse import urlparse


class DataAnalyzer:
    def __init__(self):
        self.query_count = 0
        self.stack_overflow = 0
        self.github = 0
        self.everything_else = 0

    def analyze_file(self, fileName):
        with open(fileName) as f:
            for line in f:
                self.query_count += 1

                for url in ast.literal_eval(line.split('::')[1]):
                    domain = urlparse(url).netloc.lower()

                    if 'github' in domain:
                        self.github += 1
                    elif 'stackoverflow' in domain:
                        self.stack_overflow += 1
                    else:
                        self.everything_else += 1

    def print_statistics(self):
        print("Total number of queries: " + str(self.query_count))
        print("StackOverflow count: " + str(self.stack_overflow))
        print("GitHub count: " + str(self.github))
        print("Everything else count: " + str(self.everything_else))
