import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.lancaster import LancasterStemmer

nltk.download("averaged_perceptron_tagger")
# different morphological forms of same word close treated different :(
text = "Mary closed on closing night when she was in the mood to close"

# reduce the similar words to their root form (Stemming)
st = LancasterStemmer()
stemmed_words = [st.stem(word) for word in word_tokenize(text)]
print(stemmed_words)

# let's tag their part of speech
print(nltk.pos_tag(word_tokenize(text)))
