from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from patent import get_patents
from nlp import analyze_texts, get_similarity
from collections import Counter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
def generate(data: dict):
    query = data.get("text", "").strip()

    patents = get_patents(query)
    texts = [p["abstract"] for p in patents]

    keyword_scores, X = analyze_texts(texts)

    trend = dict(Counter(keyword_scores.keys()))

    return {
        "patents": patents,
        "count": len(patents),
        "keywords": keyword_scores,
        "trend": trend
    }

@app.get("/wordcloud")
def wc():
    return FileResponse("output/wordcloud.png")

@app.get("/tfidf")
def tfidf():
    return FileResponse("output/tfidf.png")

@app.get("/similar/{idx}")
def similar(idx: int):
    return get_similarity(idx)
