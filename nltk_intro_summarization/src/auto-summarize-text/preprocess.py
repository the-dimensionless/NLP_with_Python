from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation  # list of stopwords


def parse(text):
    sents = sent_tokenize(text)
    # text sentences should be separated by 'space' after period.

    word_sents = word_tokenize(text.lower())

    _stopwards = set(stopwords.words("english") + list(punctuation))

    word_sent = [word for word in word_sents if word not in _stopwards]

    return word_sent
