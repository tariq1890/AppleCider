from bs4 import BeautifulSoup # the library to parse things
from urllib import request
import string
import csv

translator = str.maketrans(string.punctuation + string.ascii_uppercase,
                           ' ' * len(string.punctuation) + string.ascii_lowercase)

url_token_set = set()

query_urls = []

black_list_words = set()

def read_stop_words():
    with open('stan_stopwords.txt') as f:
         return set(f.read().splitlines())

def extract_from_csv(filename):
    global stop_words
    black_list_words = set()
    with open(filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csv_reader:
            if row[0] == 'NewTask':
                black_list_words = set()
                black_list_words.update(row[1].strip().split())
            else:
                #TODO: Thomas
                if len(row[1]) == 0:
                    continue
                urls = []
                query_words = set([word.lower() for word in row[0].strip().translate(translator).split()]).difference(black_list_words)
                query_words = query_words.difference(stop_words)
                for i in range(1, len(row)):
                    tokens = get_tokens_from_url(row[i])
                    if len(tokens.intersection(query_words)) > 0:
                        urls.append(row[i])
                    else:
                        if any(query_word in ' '.join(tokens) for query_word in query_words ):
                            urls.append(row[i])
                query_urls.append((row[0], urls))

    return query_urls

def writeToFile(query_urls):
    with open('url_details.txt', 'w') as outfile:
        for t in query_urls:
            outfile.write(t[0] + '::' + str(t[1]) + '\n')

def get_tokens_from_url(url):
    if '//' not in url:
        url = '%s%s' % ('http://', url)
    print(url)
    req = request.Request(url, data=b'None', headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'})
    html = request.urlopen(req).read()
    #TODO: Tariq : handle 404 URLs


    if bool(BeautifulSoup(html, "html.parser").find()):
        soup = BeautifulSoup(html, 'html.parser')
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        texts = soup.get_text(' ').strip().translate(translator).lower()
        tokens = set(texts.split())
        return tokens

    return set()

stop_words = read_stop_words()
query_urls = extract_from_csv('SpecialGoogleFinal.csv')
writeToFile(query_urls)