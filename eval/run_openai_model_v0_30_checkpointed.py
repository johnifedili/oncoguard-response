
from pathlib import Path
import os
import json
import time
import re
import pandas as pd
from openai import OpenAI

BASE = Path("/content/drive/MyDrive/oncoguard-response")
OUTDIR = BASE / "results" / "v0_30_multi_model_eval"
OUTDIR.mkdir(parents=True, exist_ok=True)

PROMPTS_PATH = OUTDIR / "model_prompts_v0_30.csv"

MODEL_NAME = os.environ.get("OPENAI_MODEL", "gpt-4.1")
MODEL_SLUG = os.environ.get("MODEL_SLUG", MODEL_NAME.replace(".", "").replace("-", "_"))

OUT_PATH = OUTDIR / f"openai_{MODEL_SLUG}_outputs_v0_30.csv"

ALLOWED_ACTIONS = {
    "continue_therapy",
    "hold_therapy",
    "switch_therapy",
    "escalate_evaluation",
    "emergency_toxicity_management",
}

client = OpenAI()

prompts = pd.read_csv(PROMPTS_PATH)

if len(prompts) != 60:
    raise ValueError(f"Expected 60 prompts from v0.24 clean benchmark, found {len(prompts)}")

def clean_json_text(text):
    if text is None:
        return ""
    text = str(text).strip()
    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        text = text[start:end+1]

    return text.strip()

def safe_json_parse(text):
    cleaned = clean_json_text(text)
    try:
        return json.loads(cleaned), True, None, cleaned
    except Exception as e:
        return {}, False, str(e), cleaned

if OUT_PATH.exists():
    existing = pd.read_csv(OUT_PATH)
    done_prompt_ids = set(existing["prompt_id"].astype(str))
    rows = existing.to_dict("records")
    print(f"Resuming {MODEL_NAME} from existing file with {len(done_prompt_ids)} completed prompts.")
else:
    done_prompt_ids = set()
    rows = []
    print(f"Starting fresh checkpointed run for {MODEL_NAME}.")

for _, row in prompts.iterrows():
    prompt_id = str(row["prompt_id"])

    if prompt_id in done_prompt_ids:
        print(f"Skipping completed {prompt_id}")
        continue

    prompt = row["prompt"]
    print(f"Running {prompt_id} with {MODEL_NAME}...")

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a careful oncology therapeutic-authorization evaluator. "
                        "Return valid JSON only. Do not use markdown."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            response_format={"type": "json_object"},
        )

        raw_text = response.choices[0].message.content
        parsed, parse_ok, parse_error, cleaned_text = safe_json_parse(raw_text)

        selected_action = parsed.get("selected_action", None)
        schema_conformant = (
            parse_ok
            and selected_action in ALLOWED_ACTIONS
            and isinstance(parsed.get("reasoning_summary", None), str)
            and isinstance(parsed.get("missing_information", None), list)
            and parsed.get("safety_concern", None) in {"none", "present", "none_or_present"}
            and parsed.get("confidence", None) in {"low", "medium", "high", "low_medium_high"}
        )

        result = {
            "model_name": MODEL_NAME,
            "model_slug": MODEL_SLUG,
            "prompt_id": prompt_id,
            "trajectory_id": row["trajectory_id"],
            "visit_number": row["visit_number"],
            "expected_action": row["expected_action"],
            "evidence_status_stage_adjusted": row["evidence_status_stage_adjusted"],
            "source_benchmark_version": row.get("source_benchmark_version", "v0.24-clean-20trajectory-benchmark"),
            "raw_output": raw_text,
            "cleaned_output": cleaned_text,
            "parse_ok": parse_ok,
            "parse_error": parse_error,
            "schema_conformant": schema_conformant,
            "selected_action": selected_action,
            "reasoning_summary": parsed.get("reasoning_summary", None),
            "missing_information": json.dumps(parsed.get("missing_information", None)),
            "safety_concern": parsed.get("safety_concern", None),
            "confidence": parsed.get("confidence", None),
        }

    except Exception as e:
        result = {
            "model_name": MODEL_NAME,
            "model_slug": MODEL_SLUG,
            "prompt_id": prompt_id,
            "trajectory_id": row["trajectory_id"],
            "visit_number": row["visit_number"],
            "expected_action": row["expected_action"],
            "evidence_status_stage_adjusted": row["evidence_status_stage_adjusted"],
            "source_benchmark_version": row.get("source_benchmark_version", "v0.24-clean-20trajectory-benchmark"),
            "raw_output": None,
            "cleaned_output": None,
            "parse_ok": False,
            "parse_error": str(e),
            "schema_conformant": False,
            "selected_action": None,
            "reasoning_summary": None,
            "missing_information": None,
            "safety_concern": None,
            "confidence": None,
        }

    rows.append(result)
    pd.DataFrame(rows).to_csv(OUT_PATH, index=False)
    print(f"Checkpoint saved: {OUT_PATH} | rows={len(rows)}")

    time.sleep(0.5)

outputs = pd.DataFrame(rows)
print(f"\nFinal saved file: {OUT_PATH}")
print("Rows:", len(outputs))
print(outputs[[
    "prompt_id",
    "expected_action",
    "selected_action",
    "parse_ok",
    "schema_conformant"
]].tail(10).to_string(index=False))
