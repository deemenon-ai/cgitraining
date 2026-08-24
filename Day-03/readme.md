okrs = pd.DataFrame([
    {"objective": "Make checkout the fastest in our category",
     "key_result": "Cut checkout time from 90s to 30s",
     "baseline": 90, "current": 52, "target": 30, "unit": "seconds", "lower_is_better": True,
     "owner": "Checkout squad", "quarter": "Q3"},
    {"objective": "Make checkout the fastest in our category",
     "key_result": "Raise checkout conversion rate",
     "baseline": 61, "current": 71, "target": 80, "unit": "%", "lower_is_better": False,
     "owner": "Checkout squad", "quarter": "Q3"},
    {"objective": "Make checkout the fastest in our category",
     "key_result": "Increase repeat-purchase rate",
     "baseline": 22, "current": 27, "target": 35, "unit": "%", "lower_is_better": False,
     "owner": "Growth squad", "quarter": "Q4"},
])
 
def progress_pct(row):
    span = row.target - row.baseline
    done = row.current - row.baseline
    pct = 0 if span == 0 else (done / span) * 100
    return round(max(0, min(100, pct)), 1)
 
okrs["progress_pct"] = okrs.apply(progress_pct, axis=1)
okrs
