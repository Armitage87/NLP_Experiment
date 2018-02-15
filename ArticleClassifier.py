import urllib
from urllib import request
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import defaultdict
from string import punctuation
from heapq import nlargest
from sklearn.neighbors import KNeighborsClassifier

vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english')
X = vectorizer.fit_transform(TEXT)

km = KMeans(n_clusters=5, init='k-means++', max_iter=100, n_init=1, verbose=True)
km.fit(X)

np.unique(km.labels_, return_counts=True)
text = {}
for i, cluster in enumerate(km.labels_):
    onedocument = doxydonkeyposts[i]
    if cluster not in text.keys():
        text[cluster] = onedocument
    else:
        text[cluster] += onedocument

_stopwords = set(stopwords.words('english') + list(punctuation)+["million", "billion", "year", "millions", "billions", "y/y", "'s", ",", "'s", "``"])

keywords = {}
counts = {}
for cluster in range(5):
    word_sent = word_tokenize(str(text)[cluster].lower())
    word_sent = [word for word in word_sent if word not in _stopwords]
    freq = FreqDist(word_sent)
    keywords[cluster] = nlargest(100, freq, key=freq.get)
    counts[cluster] = freq

uniquekeys = {}
for cluster in range(5):
    otherclusters = list(set(range(3)) - set([cluster]))
    keysotherclusters = set(keywords[otherclusters[0]]).union(set(keywords[otherclusters[1]]))
    unique = set(keywords[cluster]) - keysotherclusters
    uniquekeys[cluster] = nlargest(10, unique, key=counts[cluster].get)

article = "ARTICLE - text or scraped"
classifier = KNeighborsClassifier()
classifier.fit(X, km.labels_)
test = vectorizer.transform([article.encode('ascii', errors='ignore')])
casstest = classifier.predict(test)
print(casstest)
