import csv
import string
from urllib import request
from urllib.error import URLError
from urllib.error import HTTPError

import os
from bs4 import BeautifulSoup


class SoupyCrawler:
    def __init__(self):
        self.stop_words = self.import_stop_words('../resources/stanford_stopwords.txt')
        self.translator  = str.maketrans(string.punctuation + string.ascii_uppercase,
                           ' ' * len(string.punctuation) + string.ascii_lowercase)
        self.query_to_url_matches = []

    def import_stop_words(self, file_name):
        with open(file_name) as f:
            return set(f.read().splitlines())

    def extract_urls_from_csv_directory(self, csv_dir_name):
        black_list_words = set()

        for csv_file in os.listdir(csv_dir_name):
            if os.fsdecode(csv_file).endswith('.csv'):
                print("Mining " + os.fsdecode(csv_file))
                with open(os.path.abspath(csv_dir_name + "/" + csv_file), newline='') as csvfile:
                    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    for row in csv_reader:
                        if row[0] == 'NewTask':
                            black_list_words = set()
                            black_list_words.update(row[1].strip().split())
                        else:
                            matched_urls = self.process_row(row, black_list_words)
                            self.query_to_url_matches.append((row[0], matched_urls))

    def process_row(self, row, black_list_words):
        res = []

        if len(row[1]) == 0:
            return res

        query_keywords = set([word.lower() for word in row[0].strip().translate(self.translator).split()]).difference(black_list_words).difference(self.stop_words)
        for i in range(1, len(row)):
            print("Fetching " + row[i])
            tokens = self.get_tokens_from_url(row[i])
            if len(tokens.intersection(query_keywords)) > 0:
                res.append(row[i])
            elif any(word in ' '.join(tokens) for word in query_keywords):
                res.append(row[i])

        return res

    def get_tokens_from_url(self, url):
        tokens = set()

        # TODO: Remove enclosing quotes from url. Don't use translator as it breaks the url. For eg:- dashes are converted to whitespaces
        if '//' not in url:
            url = '%s%s' % ('http://', url)

        req = request.Request(url, data=b'None', headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'})

        try:
            html = request.urlopen(req).read()
        except HTTPError:
            with open('404Files.txt', 'a') as outfile:
                outfile.write(url + '\n')
            return tokens
        except URLError:
            print('URL Error for', url)
            return tokens
        except UnicodeEncodeError:
            print('UnicodeEncodeError for', url)
            return tokens

        if bool(BeautifulSoup(html, "html.parser").find()):
            soup = BeautifulSoup(html, 'html.parser')
            [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
            texts = soup.get_text(' ').strip().translate(self.translator).lower()
            tokens = set(texts.split())

        return tokens

    def write_to_file(self, file_name):
        with open(file_name, 'w') as outfile:
            for t in self.query_to_url_matches:
                outfile.write(t[0] + '::' + str(t[1]) + '\n')
