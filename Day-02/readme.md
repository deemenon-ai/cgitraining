import matplotlib.pyplot as plt
import numpy as np
 
tasks = list(prompts.keys())
foundational_times = [next(r["elapsed_sec"] for r in results if r["task"] == t and r["type"] == "foundational") for t in tasks]
reasoning_times    = [next(r["elapsed_sec"] for r in results if r["task"] == t and r["type"] == "reasoning") for t in tasks]
 
x = np.arange(len(tasks))
width = 0.35
 
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x - width/2, foundational_times, width, label=f"Foundational ({FOUNDATIONAL_MODEL})")
ax.bar(x + width/2, reasoning_times, width, label=f"Reasoning ({REASONING_MODEL})")
ax.set_ylabel("Latency (seconds)")
ax.set_title("Latency: Foundational vs. Reasoning Model")
ax.set_xticks(x)
ax.set_xticklabels(tasks, rotation=15)
ax.legend()
plt.tight_layout()
plt.show()
