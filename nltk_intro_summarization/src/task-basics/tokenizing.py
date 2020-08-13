import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# one time download
# nltk.download()

text = "Mary had a little lamb. Her fleece was white as snow"

sents = sent_tokenize(text)
print(sents)


# Removal of stopwards
from nltk.corpus import stopwords
from string import punctuation

# get stopwards in english and add punctuations
customStopWords = set(stopwords.words("english") + list(punctuation))
# get tokens without the stopwards
stopwords_free_tokens = [
    word for word in word_tokenize(text) if word not in customStopWords
]
print(stopwords_free_tokens)

# Identify N-grams (example bigrams)
# find collocations (words that occur together)
from nltk.collocations import *

bigram_measure = nltk.BigramCollocationFinder
# lookup even a trigram Collocation finder
finder = BigramCollocationFinder.from_words(stopwords_free_tokens)
# sort in order of frequency
print(sorted(finder.ngram_fd.items()))  # distinct bigrams and their frequencies
