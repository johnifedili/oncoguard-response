
from pathlib import Path
import os
import json
import time
import pandas as pd
from openai import OpenAI

BASE = Path("/content/drive/MyDrive/oncoguard-response")
OUTDIR = BASE / "results" / "v0_30_multi_model_eval"

PROMPTS_PATH = OUTDIR / "model_prompts_v0_30.csv"
OUT_PATH = OUTDIR / "openai_smoke_outputs_v0_30.csv"

MODEL_NAME = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
N_SMOKE = 5

ALLOWED_ACTIONS = {
    "continue_therapy",
    "hold_therapy",
    "switch_therapy",
    "escalate_evaluation",
    "emergency_toxicity_management",
}

client = OpenAI()

prompts = pd.read_csv(PROMPTS_PATH).head(N_SMOKE)

rows = []

def safe_json_parse(text):
    try:
        return json.loads(text), True, None
    except Exception as e:
        return {}, False, str(e)

for _, row in prompts.iterrows():
    prompt_id = row["prompt_id"]
    prompt = row["prompt"]

    print(f"Running {prompt_id}...")

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are a careful oncology therapeutic-authorization evaluator. Return JSON only."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
        )

        raw_text = response.choices[0].message.content

        parsed, parse_ok, parse_error = safe_json_parse(raw_text)

        selected_action = parsed.get("selected_action", None)
        schema_conformant = (
            parse_ok
            and selected_action in ALLOWED_ACTIONS
            and "reasoning_summary" in parsed
            and "missing_information" in parsed
            and "safety_concern" in parsed
            and "confidence" in parsed
        )

        rows.append({
            "model_name": MODEL_NAME,
            "prompt_id": prompt_id,
            "trajectory_id": row["trajectory_id"],
            "visit_number": row["visit_number"],
            "expected_action": row["expected_action"],
            "evidence_status_stage_adjusted": row["evidence_status_stage_adjusted"],
            "raw_output": raw_text,
            "parse_ok": parse_ok,
            "parse_error": parse_error,
            "schema_conformant": schema_conformant,
            "selected_action": selected_action,
            "reasoning_summary": parsed.get("reasoning_summary", None),
            "missing_information": json.dumps(parsed.get("missing_information", None)),
            "safety_concern": parsed.get("safety_concern", None),
            "confidence": parsed.get("confidence", None),
        })

    except Exception as e:
        rows.append({
            "model_name": MODEL_NAME,
            "prompt_id": prompt_id,
            "trajectory_id": row["trajectory_id"],
            "visit_number": row["visit_number"],
            "expected_action": row["expected_action"],
            "evidence_status_stage_adjusted": row["evidence_status_stage_adjusted"],
            "raw_output": None,
            "parse_ok": False,
            "parse_error": str(e),
            "schema_conformant": False,
            "selected_action": None,
            "reasoning_summary": None,
            "missing_information": None,
            "safety_concern": None,
            "confidence": None,
        })

    time.sleep(0.5)

outputs = pd.DataFrame(rows)
outputs.to_csv(OUT_PATH, index=False)

print(f"\nSaved: {OUT_PATH}")
print(outputs[[
    "prompt_id",
    "expected_action",
    "selected_action",
    "parse_ok",
    "schema_conformant"
]].to_string(index=False))
