
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path("/content/drive/MyDrive/oncoguard-response")
RESULTS = BASE / "results" / "freeze_v0_20_pilot"
FIGS = RESULTS / "figures"
FIGS.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Figure 1: Metric summary
# -----------------------------
metrics = pd.DataFrame({
    "metric": ["PTMAR", "AACR"],
    "value": [23.3, 93.3]
})

plt.figure(figsize=(6, 5))
plt.bar(metrics["metric"], metrics["value"])
plt.ylim(0, 100)
plt.ylabel("Rate (%)")
plt.xlabel("Metric")
plt.title("OncoGuard-Response v0.20 Pilot Metrics")

for i, value in enumerate(metrics["value"]):
    plt.text(i, value + 2, f"{value:.1f}%", ha="center")

plt.tight_layout()
out = FIGS / "figure_1_metric_summary_v0_20.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure 2: Failure taxonomy
# -----------------------------
taxonomy_path = RESULTS / "failure_taxonomy_v0_20.csv"
taxonomy = pd.read_csv(taxonomy_path)

plt.figure(figsize=(8, 5))
plt.bar(taxonomy["evidence_state"], taxonomy["failure_count"])
plt.xticks(rotation=30, ha="right")
plt.ylabel("Failure count")
plt.xlabel("Evidence-state failure mode")
plt.title("OncoGuard-Response v0.20 Failure Taxonomy")
plt.tight_layout()

out = FIGS / "figure_2_failure_taxonomy_v0_20.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")
