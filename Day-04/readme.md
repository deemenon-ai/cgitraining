# --- Extension Task 1: Add a new Key Result and initiatives
new_kr = {
    "objective": "Improve checkout UX",
    "key_result": "Reduce cart abandonment rate",
    "baseline": 70,
    "current": 60,
    "target": 50,
    "unit": "%",
    "lower_is_better": True,
    "owner": "Checkout squad",
    "quarter": "Q4",
}
# Append the new KR
okrs = pd.concat([okrs, pd.DataFrame([new_kr])], ignore_index=True)
okrs["progress_pct"] = okrs.apply(progress_pct, axis=1)

# Add corresponding initiatives to the roadmap
new_initiatives = [
    {"initiative": "Cart recovery popup", "key_result": "Reduce cart abandonment rate", "start": "2026-08-20", "end": "2026-09-10", "confidence": "High"},
    {"initiative": "Guest checkout optimization", "key_result": "Reduce cart abandonment rate", "start": "2026-09-11", "end": "2026-10-01", "confidence": "Medium"},
]
roadmap = pd.concat([roadmap, pd.DataFrame(new_initiatives)], ignore_index=True)
roadmap["start"] = pd.to_datetime(roadmap["start"]) 
roadmap["end"] = pd.to_datetime(roadmap["end"]) 
roadmap["duration_days"] = (roadmap["end"] - roadmap["start"]).dt.days

print("Added new Key Result and initiatives.")
okrs, roadmap
