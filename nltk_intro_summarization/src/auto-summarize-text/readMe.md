# Simple text summarizer using python nltk

##### Using a rule based model

#### Base steps
Scrape websites for text data using BeautifulSoup
Use nltk for munging tex-tokenization, stopword removal etc.

## High Level Procedure
    * Retrieve Text (from web),
    * Preprocess Text (parse text, format, prepare),
    * Extract Important Sentences (score, rank, retrieve)

> ( abstract extraction)

1. finding more important words -> high frequency words
2. significant scoring of sentences depends on important of words -> find sum.
3. Pick top N sentences, depending on our requirement of 
text summary length.