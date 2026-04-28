import json

def load_settings():
    try:
        with open("settings.json") as f:
            return json.load(f)
    except:
        return {"sound": True, "color": "green", "difficulty": "normal"}

def save_settings(settings):
    with open("settings.json", "w") as f:
        json.dump(settings, f)

def load_scores():
    try:
        with open("leaderboard.json") as f:
            return json.load(f)
    except:
        return []

def save_score(score):
    scores = load_scores()
    scores.append(score)
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:10]

    with open("leaderboard.json", "w") as f:
        json.dump(scores, f)