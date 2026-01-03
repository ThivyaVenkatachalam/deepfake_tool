import random

def ensemble_score(base_score):
    votes = [
        base_score,
        base_score + random.uniform(-5, 5),
        base_score + random.uniform(-5, 5)
    ]
    return round(sum(votes) / len(votes), 2)
