import urllib.request as urllib2
from bs4 import BeautifulSoup


def getText(article_url):
    page = urllib2.urlopen(article_url).read().decode("utf-8", "ignore")
    soup = BeautifulSoup(page, "lxml")
    # print(soup) # prints whole page

    # get first article
    # article = soup.find("article")
    # print(article.text)  # display article content

    # get list of articles on the page
    articles = soup.findAll("article")

    combined_text = " ".join(map(lambda p: p.text, soup.findAll("article")))
    print(combined_text)  # print article texts.

    # encode properly and remove irrelevant characters.
    combined_text.encode("ascii", errors="replace")
    combined_text.replace("?", " ")

    return combined_text
