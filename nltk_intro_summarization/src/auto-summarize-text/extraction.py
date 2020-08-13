from nltk.probability import FreqDist  # table of word frequency
from heapq import nlargest  # to get top N sorted
from collections import defaultdict
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation  # list of stopwords


def extract(text, n):
    sents = sent_tokenize(text)

    assert n <= len(sents)

    word_sent = word_tokenize(text.lower())
    _stopwards = set(stopwords.words("english") + list(punctuation))
    word_sent = [word for word in word_sent if word not in _stopwards]

    freq = FreqDist(word_sent)  # expect a dict of words : frequencies

    # higher the frequency, important the words
    ranking = defaultdict(int)

    for i, sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]

    # input: number of sentences, main list, sort by value
    top10 = nlargest(n, ranking, key=ranking.get)

    summary = [sents[j] for j in sorted(top10)]

    return summary
