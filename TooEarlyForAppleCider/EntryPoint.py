from TooEarlyForAppleCider.SoupyCrawler import SoupyCrawler

if __name__ == '__main__':
    crawler = SoupyCrawler()
    crawler.extract_urls_from_csv('../resources/SpecialGoogleFinal.csv')
    crawler.write_to_file()
