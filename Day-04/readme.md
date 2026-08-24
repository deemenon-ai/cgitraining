# --- Extension Task 2: Confidence filter (interactive if ipywidgets available)
try:
    import ipywidgets as widgets
    from IPython.display import display, clear_output
    has_widgets = True
except Exception:
    has_widgets = False

def plot_roadmap(filtered_roadmap):
    import matplotlib.dates as mdates
    fig, ax = plt.subplots(figsize=(10, 5))
    conf_color = {"High": "#2C5F2D", "Medium": "#E7B10A", "Low": "#B85042"}
    krs = filtered_roadmap["key_result"].unique()
    y = 0
    for kr in krs:
        rows = filtered_roadmap[filtered_roadmap["key_result"] == kr]
        for _, r in rows.iterrows():
            ax.barh(y, r.duration_days, left=r.start, height=0.6,
                    color=conf_color.get(r.confidence, "#888888"), edgecolor="white")
            ax.text(r.start, y, f"  {r.initiative}", va="center", ha="left",
                    fontsize=8.5, color="white", fontweight="bold")
            y += 1
        y += 0.6

    ax.set_yticks([]); ax.invert_yaxis()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax.set_title("Outcome-based roadmap: initiatives grouped by Key Result", fontsize=13, fontweight="bold")
    handles = [plt.Rectangle((0,0),1,1, color=c) for c in conf_color.values()]
    ax.legend(handles, conf_color.keys(), title="Confidence", loc="upper right")
    plt.tight_layout()
    plt.show()


def update_plot(confidence):
    if confidence == "All":
        filtered = roadmap.copy()
    else:
        filtered = roadmap[roadmap["confidence"] == confidence]
    filtered = filtered.copy()
    filtered["start"] = pd.to_datetime(filtered["start"]) 
    filtered["end"] = pd.to_datetime(filtered["end"]) 
    filtered["duration_days"] = (filtered["end"] - filtered["start"]).dt.days
    if has_widgets:
        clear_output(wait=True)
        display(filter_widget, out)
    plot_roadmap(filtered)

if has_widgets:
    options = ["All"] + sorted(roadmap["confidence"].dropna().unique().tolist())
    filter_widget = widgets.Dropdown(options=options, value="All", description="Confidence:")
    out = widgets.interactive_output(update_plot, {"confidence": filter_widget})
    display(filter_widget, out)
else:
    print("ipywidgets not available — showing full roadmap (non-interactive)")
    plot_roadmap(roadmap)
