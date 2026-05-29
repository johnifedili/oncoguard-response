
from pathlib import Path
import os
import json
import time
import re
import pandas as pd
from google import genai
from google.genai import types

BASE = Path("/content/drive/MyDrive/oncoguard-response")
OUTDIR = BASE / "results" / "v0_30_multi_model_eval"
OUTDIR.mkdir(parents=True, exist_ok=True)

PROMPTS_PATH = OUTDIR / "model_prompts_v0_30.csv"

GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.1-pro-preview")
MODEL_SLUG = os.environ.get("MODEL_SLUG", "gemini31pro")

OUT_PATH = OUTDIR / f"google_{MODEL_SLUG}_outputs_v0_30.csv"

ALLOWED_ACTIONS = {
    "continue_therapy",
    "hold_therapy",
    "switch_therapy",
    "escalate_evaluation",
    "emergency_toxicity_management",
}

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

prompts = pd.read_csv(PROMPTS_PATH)

if len(prompts) != 60:
    raise ValueError(f"Expected 60 prompts from v0.24 clean benchmark, found {len(prompts)}")

SYSTEM_PROMPT = (
    "You are a careful oncology therapeutic-authorization evaluator. "
    "Return valid JSON only. Do not use markdown. "
    "Your JSON must contain selected_action, reasoning_summary, missing_information, safety_concern, and confidence."
)

def extract_text_from_gemini_response(response):
    # First try standard SDK convenience property.
    try:
        if response.text:
            return response.text
    except Exception:
        pass

    # Fallback: manually extract candidate text parts.
    texts = []
    try:
        for candidate in response.candidates or []:
            content = getattr(candidate, "content", None)
            parts = getattr(content, "parts", None) if content else None
            if not parts:
                continue
            for part in parts:
                text = getattr(part, "text", None)
                if text:
                    texts.append(text)
    except Exception:
        pass

    return "\n".join(texts).strip() if texts else None

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
    print(f"Resuming {GEMINI_MODEL} from existing file with {len(done_prompt_ids)} completed prompts.")
else:
    done_prompt_ids = set()
    rows = []
    print(f"Starting fresh checkpointed run for {GEMINI_MODEL}.")

for _, row in prompts.iterrows():
    prompt_id = str(row["prompt_id"])

    if prompt_id in done_prompt_ids:
        print(f"Skipping completed {prompt_id}")
        continue

    prompt = row["prompt"]
    print(f"Running {prompt_id} with {GEMINI_MODEL}...")

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0,
                response_mime_type="application/json",
                max_output_tokens=1000,
            ),
        )

        raw_text = extract_text_from_gemini_response(response)
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
            "provider": "google",
            "model_name": GEMINI_MODEL,
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
            "provider": "google",
            "model_name": GEMINI_MODEL,
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
