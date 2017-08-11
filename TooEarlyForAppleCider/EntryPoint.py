from TooEarlyForAppleCider.DataAnalyzer import DataAnalyzer
from TooEarlyForAppleCider.SoupyCrawler import SoupyCrawler

if __name__ == '__main__':
    crawler = SoupyCrawler()
    crawler.extract_urls_from_csv_directory('../resources/SpecialGoogleFinalSplit/')
    crawler.write_to_file('data_file.txt')

    analysis = DataAnalyzer()
    analysis.analyze_file('data_file.txt')
    analysis.print_statistics()
