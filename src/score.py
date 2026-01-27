import json

def load_scores():
    try:
        with open('score.json', 'r') as f_score: #retrieve scores from json file
            return json.load(f_score)
    except FileNotFoundError:
        return {}

