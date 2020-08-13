# collecting articles from data blog

import urllib.request as urllib2
from bs4 import BeautifulSoup


def getText(p):
    p.text.encode("ascii", errors="replace")
    p.text.replace("?", " ")
    return p.text


def getDoxyArticles(test_url):
    request = urllib2.Request(test_url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response)
    mydivs = soup.findAll("div", {"class": "post-body"})

    posts = []

    for div in mydivs:
        posts += map(lambda p : getText(p), div.findAll("li"))

    return posts


def get_all_urls(url, links):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response)
    for a in soup.findAll("a"):
        try:
            url = a["href"]
            title = a["title"]
            if title == "Older Posts":
                print("Page Found : ", title, url)
                links.append(url)
                get_all_urls(url, links)
        except:
            title = ""


blog_url = "https://doxydonkey.blogspot.com/"
links = []
get_all_urls(blog_url, links)

all_posts = []

for link in links:
    all_posts += getDoxyArticles(link)

print(all_posts)
