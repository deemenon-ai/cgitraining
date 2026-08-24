conf_color = {"High": "#2C5F2D", "Medium": "#E7B10A", "Low": "#B85042"}
krs = roadmap["key_result"].unique()
fig, ax = plt.subplots(figsize=(10, 5))
 
y = 0
yticks, yticklabels = [], []
for kr in krs:
    rows = roadmap[roadmap["key_result"] == kr]
    for _, r in rows.iterrows():
        ax.barh(y, r.duration_days, left=r.start, height=0.6,
                color=conf_color[r.confidence], edgecolor="white")
        ax.text(r.start, y, f"  {r.initiative}", va="center", ha="left",
                fontsize=8.5, color="white", fontweight="bold")
        yticks.append(y); yticklabels.append("")
        y += 1
    y += 0.6
 
ax.set_yticks([]); ax.invert_yaxis()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax.set_title("Outcome-based roadmap: initiatives grouped by Key Result", fontsize=13, fontweight="bold")
handles = [plt.Rectangle((0,0),1,1, color=c) for c in conf_color.values()]
ax.legend(handles, conf_color.keys(), title="Confidence", loc="upper right")
 
# annotate KR group boundaries
running = 0
for kr in krs:
    n = len(roadmap[roadmap["key_result"] == kr])
    ax.axhline(running - 0.3, color="#999999", linewidth=0.6, linestyle="--")
    running += n + 0.6
plt.tight_layout()
plt.show()
