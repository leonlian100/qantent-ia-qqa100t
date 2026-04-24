import matplotlib
matplotlib.use("Agg")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

X_GLOBAL = None

def analyze_texts(texts):
    global X_GLOBAL

    vec = TfidfVectorizer(stop_words="english", max_features=20)
    X = vec.fit_transform(texts)

    X_GLOBAL = X

    keywords = vec.get_feature_names_out()
    scores = X.sum(axis=0).A1

    keyword_scores = dict(zip(keywords, scores))

    os.makedirs("output", exist_ok=True)

    WordCloud().generate(" ".join(texts)).to_file("output/wordcloud.png")

    plt.figure()
    plt.bar(keyword_scores.keys(), keyword_scores.values())
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/tfidf.png")
    plt.close()

    return keyword_scores, X

def get_similarity(idx):
    global X_GLOBAL
    sim = cosine_similarity(X_GLOBAL[idx], X_GLOBAL)[0]
    return sim.argsort()[-5:].tolist()
