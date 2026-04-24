import json

def get_patents(query):
    with open("data/patents.json", encoding="utf-8") as f:
        data = json.load(f)

    return [
        p for p in data
        if query.lower() in p["abstract"].lower()
    ][:50]
