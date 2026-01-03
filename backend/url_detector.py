import whois
from datetime import datetime

def check_url(url):
    try:
        w = whois.whois(url)
        created = w.creation_date
        if isinstance(created, list):
            created = created[0]

        age = (datetime.now() - created).days
        verdict = "🔴 Suspicious" if age < 90 else "🟢 Safe"

        return {"age": age, "verdict": verdict}
    except:
        return {"age": None, "verdict": "⚠️ Unknown"}
