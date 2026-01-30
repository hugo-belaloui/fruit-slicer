import json

def load_scores():
    try:
        with open('score.json', 'r') as f_score: #retrieve scores from json file
            return json.load(f_score)
    except FileNotFoundError:
        return {}

def add_scores(scoring):
    try:
        with open('score.json', 'w') as f_score: #retrieve scores from json file
            return json.dump(scoring, f_score, indent=4)
    except FileNotFoundError:
        return {}