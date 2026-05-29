
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path("/content/drive/MyDrive/oncoguard-response")
RESULTS = BASE / "results" / "v0_22_safety_margin_policy"
FIGS = RESULTS / "figures"
FIGS.mkdir(parents=True, exist_ok=True)

summary_path = RESULTS / "multi_policy_summary_v0_22_safety_margin.csv"
summary = pd.read_csv(summary_path)

policy_order = ["permissive", "standard", "conservative_margin"]
summary["policy_name"] = pd.Categorical(
    summary["policy_name"],
    categories=policy_order,
    ordered=True
)
summary = summary.sort_values("policy_name")

display_names = {
    "permissive": "Permissive",
    "standard": "Standard",
    "conservative_margin": "Conservative\nmargin",
}
summary["policy_label"] = summary["policy_name"].map(display_names)

# -----------------------------
# Helper function
# -----------------------------
def save_bar(metric_col, ylabel, title, filename):
    plt.figure(figsize=(7, 5))
    plt.bar(summary["policy_label"], summary[metric_col])
    plt.ylim(0, 110)
    plt.ylabel(ylabel)
    plt.xlabel("Policy")
    plt.title(title)

    for i, value in enumerate(summary[metric_col]):
        y = value + 2 if value <= 95 else value - 8
        plt.text(i, y, f"{value:.1f}%", ha="center")

    plt.tight_layout()
    out = FIGS / filename
    plt.savefig(out, dpi=300)
    plt.show()
    print(f"Saved: {out}")

# -----------------------------
# Figure 1: PTMAR by policy
# -----------------------------
save_bar(
    "ptmar_percent",
    "PTMAR (%)",
    "OncoGuard-Response v0.22 PTMAR by Policy",
    "figure_1_v0_22_ptmar_by_policy.png"
)

# -----------------------------
# Figure 2: AACR by policy
# -----------------------------
save_bar(
    "aacr_percent",
    "AACR (%)",
    "OncoGuard-Response v0.22 AACR by Policy",
    "figure_2_v0_22_aacr_by_policy.png"
)

# -----------------------------
# Figure 3: Deferral by policy
# -----------------------------
save_bar(
    "defer_rate_percent",
    "Defer rate (%)",
    "OncoGuard-Response v0.22 Deferral by Policy",
    "figure_3_v0_22_defer_rate_by_policy.png"
)

# -----------------------------
# Figure 4: Unsafe authorization by policy
# -----------------------------
save_bar(
    "unsafe_authorization_rate_percent",
    "Unsafe authorization (%)",
    "OncoGuard-Response v0.22 Unsafe Authorization by Policy",
    "figure_4_v0_22_unsafe_authorization_by_policy.png"
)

# -----------------------------
# Figure 5: Over-deferral by policy
# -----------------------------
save_bar(
    "over_deferral_rate_percent",
    "Over-deferral (%)",
    "OncoGuard-Response v0.22 Over-Deferral by Policy",
    "figure_5_v0_22_over_deferral_by_policy.png"
)

# -----------------------------
# Figure 6: Safety-margin trigger count
# -----------------------------
plt.figure(figsize=(7, 5))
plt.bar(summary["policy_label"], summary["safety_margin_trigger_count"])
plt.ylabel("Safety-margin trigger count")
plt.xlabel("Policy")
plt.title("OncoGuard-Response v0.22 Safety-Margin Triggers")

for i, value in enumerate(summary["safety_margin_trigger_count"]):
    plt.text(i, value + 0.2, f"{int(value)}", ha="center")

plt.tight_layout()
out = FIGS / "figure_6_v0_22_safety_margin_triggers.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure 7: Combined policy comparison
# -----------------------------
metrics = [
    "ptmar_percent",
    "aacr_percent",
    "defer_rate_percent",
    "unsafe_authorization_rate_percent",
    "over_deferral_rate_percent",
    "correct_authorization_rate_percent",
]

metric_labels = {
    "ptmar_percent": "PTMAR",
    "aacr_percent": "AACR",
    "defer_rate_percent": "Defer rate",
    "unsafe_authorization_rate_percent": "Unsafe authorization",
    "over_deferral_rate_percent": "Over-deferral",
    "correct_authorization_rate_percent": "Correct authorization",
}

x = range(len(metrics))
bar_width = 0.25

plt.figure(figsize=(12, 6))

for idx, policy in enumerate(policy_order):
    values = []
    for metric in metrics:
        value = summary.loc[summary["policy_name"] == policy, metric].iloc[0]
        values.append(value)

    positions = [i + (idx - 1) * bar_width for i in x]
    label = display_names[policy].replace("\n", " ")
    plt.bar(positions, values, width=bar_width, label=label)

plt.xticks(list(x), [metric_labels[m] for m in metrics], rotation=20, ha="right")
plt.ylim(0, 110)
plt.ylabel("Rate (%)")
plt.xlabel("Metric")
plt.title("OncoGuard-Response v0.22 Safety-Margin Policy Comparison")
plt.legend(title="Policy")
plt.tight_layout()

out = FIGS / "figure_7_v0_22_multi_policy_comparison.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure index
# -----------------------------
figure_index = pd.DataFrame([
    {
        "figure_id": "Figure 1",
        "filename": "figure_1_v0_22_ptmar_by_policy.png",
        "title": "PTMAR by policy",
        "description": "Policy-level comparison of premature therapy misuse action rate."
    },
    {
        "figure_id": "Figure 2",
        "filename": "figure_2_v0_22_aacr_by_policy.png",
        "title": "AACR by policy",
        "description": "Policy-level comparison of authorization alignment contract rate."
    },
    {
        "figure_id": "Figure 3",
        "filename": "figure_3_v0_22_defer_rate_by_policy.png",
        "title": "Deferral by policy",
        "description": "Policy-level comparison of escalation or deferral rate."
    },
    {
        "figure_id": "Figure 4",
        "filename": "figure_4_v0_22_unsafe_authorization_by_policy.png",
        "title": "Unsafe authorization by policy",
        "description": "Policy-level comparison of unsafe continuation despite non-authorized status."
    },
    {
        "figure_id": "Figure 5",
        "filename": "figure_5_v0_22_over_deferral_by_policy.png",
        "title": "Over-deferral by policy",
        "description": "Policy-level comparison of additional deferral when continuation was otherwise authorized."
    },
    {
        "figure_id": "Figure 6",
        "filename": "figure_6_v0_22_safety_margin_triggers.png",
        "title": "Safety-margin triggers",
        "description": "Number of extra reassessment events triggered by the conservative-margin policy."
    },
    {
        "figure_id": "Figure 7",
        "filename": "figure_7_v0_22_multi_policy_comparison.png",
        "title": "Combined v0.22 multi-policy comparison",
        "description": "Grouped comparison of PTMAR, AACR, defer rate, unsafe authorization, over-deferral, and correct authorization across policies."
    },
])

index_out = FIGS / "figure_index_v0_22.csv"
figure_index.to_csv(index_out, index=False)
print(f"Saved: {index_out}")
