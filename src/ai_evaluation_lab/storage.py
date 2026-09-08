"""JSON persistence for AI Evaluation Lab."""

import json
from dataclasses import asdict
from pathlib import Path

from .evaluator import Evaluation


def save_evaluation(evaluation: Evaluation, path: str | Path) -> Path:
    """Save one evaluation as readable UTF-8 JSON and return its path."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    payload = asdict(evaluation)
    payload["overall_score"] = evaluation.scores.overall_score

    output_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return output_path


def load_evaluation(path: str | Path) -> dict[str, object]:
    """Load a stored evaluation for inspection or later processing."""
    input_path = Path(path)
    return json.loads(input_path.read_text(encoding="utf-8"))
