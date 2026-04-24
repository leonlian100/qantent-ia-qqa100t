import matplotlib
matplotlib.use("Agg")

import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

FONT_PATH = "fonts/NotoSansTC-Regular.otf"

def tokenize(text):
    return " ".join(jieba.cut(text))

def analyze_texts(texts):
    # 🔥 中文斷詞
    texts_cut = [tokenize(t) for t in texts]

    vectorizer = TfidfVectorizer(max_features=20)
    X = vectorizer.fit_transform(texts_cut)

    keywords = vectorizer.get_feature_names_out()
    scores = X.sum(axis=0).A1

    keyword_scores = dict(zip(keywords, scores))

    os.makedirs("output", exist_ok=True)

    # 🔥 文字雲（支援中文）
    WordCloud(
        font_path=FONT_PATH,
        width=800,
        height=400
    ).generate(" ".join(texts_cut)).to_file("output/wordcloud.png")

    # 🔥 matplotlib 中文
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["Noto Sans TC"]

    plt.figure()
    plt.bar(keyword_scores.keys(), keyword_scores.values())
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/tfidf.png")
    plt.close()

    return keyword_scores
