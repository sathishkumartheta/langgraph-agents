import re
import ast
import json

def extract_reason(response_text):
    # Clean wrapping quotes or brackets
    response_text = response_text.strip().strip('\'"[]()')

    # Try parsing as JSON first
    try:
        data = json.loads(response_text)
        return data.get("reason", "").strip()
    except json.JSONDecodeError:
        pass

    # Fallback to ast.literal_eval (safer than eval)
    try:
        data = ast.literal_eval(response_text)
        if isinstance(data, dict):
            return data.get("reason", "").strip()
    except Exception:
        pass

    # Fallback to regex
    match = re.search(r'"reason"\s*:\s*"([^"]+)"', response_text)
    if match:
        return match.group(1).strip()

    # Nothing matched
    return ""

