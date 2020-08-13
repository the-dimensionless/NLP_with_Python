import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# wordnet is a lexicon (thesaurus)
# synset is one single definition of a word

from nltk.corpus import wordnet as wn

# multiple definition
""" for ss in wn.synsets("bass"):
    print(ss, ss.definition()) """

# we use a sentence with two different meanings of word bass

from nltk.wsd import lesk  # algo for word sense disambiguation

# input: set of words, word we want to inspect.
# return: word definition in the given context.
sensel = lesk(word_tokenize("Sing in a lower tone, along with the bass"), "bass")
print(sensel, sensel.definition())  # expecting music related definition

print("-----------change sentence-----------")

sensel = lesk(word_tokenize("This sea bass was really hard to catch"), "bass")
print(sensel, sensel.definition())  # expecting definition of fish
