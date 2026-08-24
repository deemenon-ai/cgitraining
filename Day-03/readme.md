fig, ax = plt.subplots(figsize=(9, 4))
y_pos = np.arange(len(okrs))
colors = ["#2C5F2D" if p >= 70 else "#E7B10A" if p >= 40 else "#B85042" for p in okrs.progress_pct]
 
ax.barh(y_pos, okrs.progress_pct, color=colors, height=0.5)
ax.barh(y_pos, 100, color="#EEEEEE", height=0.5, zorder=0)
ax.barh(y_pos, okrs.progress_pct, color=colors, height=0.5, zorder=1)
ax.set_yticks(y_pos)
ax.set_yticklabels(okrs.key_result)
ax.set_xlim(0, 100)
ax.set_xlabel("Progress toward target (%)")
ax.set_title("Key Result progress — 🟢 on track  🟡 at risk  🔴 behind", fontsize=12, fontweight="bold")
for i, (p, cur, tgt, unit) in enumerate(zip(okrs.progress_pct, okrs.current, okrs.target, okrs.unit)):
    ax.text(102, i, f"{cur}{unit} → target {tgt}{unit}", va="center", fontsize=9)
plt.tight_layout()
plt.show()
 
