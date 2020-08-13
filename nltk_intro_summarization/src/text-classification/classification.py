
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

def classify(list_of_articles):
    vec = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english')
    X = vec.fit_transform(list_of_articles)

    km = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 100, n_init = 1, verbose = True)
    km.fit(X)

    unique = np.unique(km.labels_, return_counts = True)