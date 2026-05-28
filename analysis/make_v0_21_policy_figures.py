
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path("/content/drive/MyDrive/oncoguard-response")
RESULTS = BASE / "results" / "v0_21_multi_policy"
FIGS = RESULTS / "figures"
FIGS.mkdir(parents=True, exist_ok=True)

summary_path = RESULTS / "multi_policy_summary_v0_21_adjusted_scored.csv"
summary = pd.read_csv(summary_path)

# Ensure policy order
policy_order = ["permissive", "standard", "conservative"]
summary["policy_name"] = pd.Categorical(
    summary["policy_name"],
    categories=policy_order,
    ordered=True
)
summary = summary.sort_values("policy_name")

# -----------------------------
# Figure 1: PTMAR by policy
# -----------------------------
plt.figure(figsize=(7, 5))
plt.bar(summary["policy_name"], summary["ptmar_percent"])
plt.ylim(0, 100)
plt.ylabel("PTMAR (%)")
plt.xlabel("Policy")
plt.title("OncoGuard-Response v0.21 PTMAR by Policy")

for i, value in enumerate(summary["ptmar_percent"]):
    plt.text(i, value + 2, f"{value:.1f}%", ha="center")

plt.tight_layout()
out = FIGS / "figure_1_v0_21_ptmar_by_policy.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure 2: AACR by policy
# -----------------------------
plt.figure(figsize=(7, 5))
plt.bar(summary["policy_name"], summary["aacr_percent"])
plt.ylim(0, 100)
plt.ylabel("AACR (%)")
plt.xlabel("Policy")
plt.title("OncoGuard-Response v0.21 AACR by Policy")

for i, value in enumerate(summary["aacr_percent"]):
    plt.text(i, value + 2 if value <= 95 else value - 8, f"{value:.1f}%", ha="center")

plt.tight_layout()
out = FIGS / "figure_2_v0_21_aacr_by_policy.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure 3: Defer rate by policy
# -----------------------------
plt.figure(figsize=(7, 5))
plt.bar(summary["policy_name"], summary["defer_rate_percent"])
plt.ylim(0, 100)
plt.ylabel("Defer rate (%)")
plt.xlabel("Policy")
plt.title("OncoGuard-Response v0.21 Deferral by Policy")

for i, value in enumerate(summary["defer_rate_percent"]):
    plt.text(i, value + 2, f"{value:.1f}%", ha="center")

plt.tight_layout()
out = FIGS / "figure_3_v0_21_defer_rate_by_policy.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure 4: Unsafe authorization by policy
# -----------------------------
plt.figure(figsize=(7, 5))
plt.bar(summary["policy_name"], summary["unsafe_authorization_rate_percent"])
plt.ylim(0, 100)
plt.ylabel("Unsafe authorization (%)")
plt.xlabel("Policy")
plt.title("OncoGuard-Response v0.21 Unsafe Authorization by Policy")

for i, value in enumerate(summary["unsafe_authorization_rate_percent"]):
    plt.text(i, value + 2, f"{value:.1f}%", ha="center")

plt.tight_layout()
out = FIGS / "figure_4_v0_21_unsafe_authorization_by_policy.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure 5: Combined policy comparison
# -----------------------------
metrics = [
    "ptmar_percent",
    "aacr_percent",
    "defer_rate_percent",
    "unsafe_authorization_rate_percent",
    "correct_authorization_rate_percent",
]

metric_labels = {
    "ptmar_percent": "PTMAR",
    "aacr_percent": "AACR",
    "defer_rate_percent": "Defer rate",
    "unsafe_authorization_rate_percent": "Unsafe authorization",
    "correct_authorization_rate_percent": "Correct authorization",
}

long = summary.melt(
    id_vars=["policy_name"],
    value_vars=metrics,
    var_name="metric",
    value_name="percent"
)

long["metric_label"] = long["metric"].map(metric_labels)

# Grouped bar plot using plain matplotlib
policies = policy_order
labels = [metric_labels[m] for m in metrics]

x = range(len(labels))
bar_width = 0.25

plt.figure(figsize=(11, 6))

for idx, policy in enumerate(policies):
    values = []
    for metric in metrics:
        value = summary.loc[summary["policy_name"] == policy, metric].iloc[0]
        values.append(value)

    positions = [i + (idx - 1) * bar_width for i in x]
    plt.bar(positions, values, width=bar_width, label=policy)

plt.xticks(list(x), labels, rotation=20, ha="right")
plt.ylim(0, 110)
plt.ylabel("Rate (%)")
plt.xlabel("Metric")
plt.title("OncoGuard-Response v0.21 Multi-Policy Comparison")
plt.legend(title="Policy")
plt.tight_layout()

out = FIGS / "figure_5_v0_21_multi_policy_comparison.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure index
# -----------------------------
figure_index = pd.DataFrame([
    {
        "figure_id": "Figure 1",
        "filename": "figure_1_v0_21_ptmar_by_policy.png",
        "title": "PTMAR by policy",
        "description": "Policy-level comparison of premature therapy misuse action rate."
    },
    {
        "figure_id": "Figure 2",
        "filename": "figure_2_v0_21_aacr_by_policy.png",
        "title": "AACR by policy",
        "description": "Policy-level comparison of authorization alignment contract rate."
    },
    {
        "figure_id": "Figure 3",
        "filename": "figure_3_v0_21_defer_rate_by_policy.png",
        "title": "Deferral by policy",
        "description": "Policy-level comparison of escalation/deferral rate."
    },
    {
        "figure_id": "Figure 4",
        "filename": "figure_4_v0_21_unsafe_authorization_by_policy.png",
        "title": "Unsafe authorization by policy",
        "description": "Policy-level comparison of unsafe continuation despite non-authorized status."
    },
    {
        "figure_id": "Figure 5",
        "filename": "figure_5_v0_21_multi_policy_comparison.png",
        "title": "Combined multi-policy comparison",
        "description": "Grouped comparison of PTMAR, AACR, defer rate, unsafe authorization, and correct authorization across permissive, standard, and conservative policies."
    },
])

index_out = FIGS / "figure_index_v0_21.csv"
figure_index.to_csv(index_out, index=False)
print(f"Saved: {index_out}")
