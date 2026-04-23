import json

def load_data(path="data/knowledge.json"):
    with open(path, "r") as f:
        return json.load(f)