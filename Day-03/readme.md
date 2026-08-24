roadmap = pd.DataFrame([
    {"initiative": "One-click checkout",        "key_result": "Cut checkout time from 90s to 30s",
     "start": "2026-07-01", "end": "2026-08-15", "confidence": "High"},
    {"initiative": "Guest checkout (no signup)", "key_result": "Cut checkout time from 90s to 30s",
     "start": "2026-08-01", "end": "2026-09-15", "confidence": "Medium"},
    {"initiative": "Saved-payment autofill",     "key_result": "Raise checkout conversion rate",
     "start": "2026-07-15", "end": "2026-08-30", "confidence": "High"},
    {"initiative": "Trust badges & reviews",     "key_result": "Raise checkout conversion rate",
     "start": "2026-09-01", "end": "2026-09-30", "confidence": "Medium"},
    {"initiative": "Referral program",           "key_result": "Increase repeat-purchase rate",
     "start": "2026-10-01", "end": "2026-11-15", "confidence": "Low"},
    {"initiative": "Post-purchase loyalty tier",  "key_result": "Increase repeat-purchase rate",
     "start": "2026-11-01", "end": "2026-12-15", "confidence": "Medium"},
])
roadmap["start"] = pd.to_datetime(roadmap["start"])
roadmap["end"] = pd.to_datetime(roadmap["end"])
roadmap["duration_days"] = (roadmap["end"] - roadmap["start"]).dt.days
roadmap
