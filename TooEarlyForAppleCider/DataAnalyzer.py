import ast
from urllib.parse import urlparse


class DataAnalyzer:
    def __init__(self):
        self.query_count = 0
        self.inspired_count = 0;
        self.stack_overflow = 0
        self.github = 0
        self.everything_else = 0

    def analyze_file(self, fileName):
        with open(fileName) as f:
            for line in f:
                self.query_count += 1

                urls = ast.literal_eval(line.split('::')[1])

                if len(urls) > 0:
                    self.inspired_count += 1
                    for url in urls:
                        if 'github' in url:
                            self.github += 1
                        elif 'stackoverflow' in url:
                            self.stack_overflow += 1
                        else:
                            self.everything_else += 1

    def print_statistics(self):
        print("Total number of queries: " + str(self.query_count))
        print("Total number of inspired queries: " + str(self.inspired_count))
        print("StackOverflow count: " + str(self.stack_overflow))
        print("GitHub count: " + str(self.github))
        print("Everything else count: " + str(self.everything_else))


if __name__ == '__main__':
    analyzer = DataAnalyzer()
    analyzer.analyze_file('../run1/data_file_aggregated.txt')
    analyzer.print_statistics()
