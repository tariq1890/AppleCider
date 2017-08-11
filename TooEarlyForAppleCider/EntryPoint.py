from TooEarlyForAppleCider.DataAnalyzer import DataAnalyzer
from TooEarlyForAppleCider.SoupyCrawler import SoupyCrawler

if __name__ == '__main__':
    crawler = SoupyCrawler()
    crawler.import_stop_words('../resources/stanford_stopwords.txt')
    crawler.import_bad_urls(['ErrorUrls.txt'])
    crawler.extract_urls_from_csv_directory('../resources/splits/')
    crawler.write_to_file('data_file.txt')

    analysis = DataAnalyzer()
    analysis.analyze_file('data_file.txt')
    analysis.print_statistics()
