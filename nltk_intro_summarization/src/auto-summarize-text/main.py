from retrieve import getText
from preprocess import parse
from extraction import extract

article_url = "https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/"
summary = extract(getText(article_url), 3)

print("Summary -> \n")
for i in summary:
    print(i + "\n")
