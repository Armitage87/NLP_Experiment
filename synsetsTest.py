import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.collocations import *
from nltk.corpus import wordnet as wn
from nltk.stem.lancaster import LancasterStemmer
from nltk.wsd import lesk
st = LancasterStemmer()
customStopWords = set(stopwords.words('english')+list(punctuation))

text = "Mary had a little lamb. Her fleece was white as snow"
sents = sent_tokenize(text)
print(sents)
words = [word_tokenize(sent) for sent in sents]
print(words)
wordsWOStopwords = [word for word in word_tokenize(text) if word not in customStopWords]
print(wordsWOStopwords)
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(wordsWOStopwords)
print(sorted(finder.ngram_fd.items()))
"""
text2 = "Mary closed on closing night when she was in the mood to close."
stemmedWords = [st.stem(word) for word in word_tokenize(text2)]
print(stemmedWords)
tre = nltk.pos_tag(word_tokenize(text2))
print(tre)
"""
"""
for ss in wn.synsets('bass'):
    print(ss, ss.definition())
"""
sensel = lesk(word_tokenize("Sing in a lower tone, along with the bass"), 'bass')
print(sensel, sensel.definition())
