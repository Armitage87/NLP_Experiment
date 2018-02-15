import urllib
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

articleurl = "https://www.washingtonpost.com/news/politics/wp/2017/11/16/texas-sheriff-is-on-the-hunt-for-driver-with-profane-anti-trump-window-sticker/?hpid=hp_no-name_hp-in-the-news%3Apage%2Fin-the-news&utm_term=.12d3f06546e9"


def gettexttapo(url):
    with urllib.request.urlopen(url) as f:
        output = f.read().decode('utf-8', 'ignore')
    soup = BeautifulSoup(output, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
    return text.encode('ascii', errors='replace')
    
    def suummarize(text, n):
    sents = sent_tokenize(text)

    assert n <= len(sents)
    word_sent = word_tokenize(text.lower())
    _stopwords = set(stopwords.words('english') + list(punctuation))

    word_sent = [word for word in word_sent if word not in _stopwords]
    freq = FreqDist(word_sent)

    ranking = defaultdict(int)

    for i, sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]

    sents_idx = nlargest(n, ranking, key=ranking.get)
    return [sents[j] for j in sorted(sents_idx)]

sumkk = suummarize(text, 5)
print(sumkk)
