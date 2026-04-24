import requests
from bs4 import BeautifulSoup
import json

def crawl(query):
    url = f"https://patents.google.com/?q={query}"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    results = []

    for item in soup.select("search-result-item")[:20]:
        title = item.select_one("h3").text if item.select_one("h3") else ""
        abstract = item.select_one(".abstract").text if item.select_one(".abstract") else ""

        results.append({
            "title": title,
            "abstract": abstract
        })

    with open("data/patents.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

crawl("robot")
