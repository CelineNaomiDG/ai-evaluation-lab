"""Core data model for transparent AI response evaluation."""

from dataclasses import dataclass, fields

MIN_SCORE = 1
MAX_SCORE = 5


@dataclass(frozen=True)
class EvaluationScores:
    """Scores for the seven criteria used by AI Evaluation Lab v1."""

    correctness: int
    factuality: int
    instruction_following: int
    relevance: int
    completeness: int
    clarity: int
    safety: int

    def __post_init__(self) -> None:
        """Reject booleans, non-integers and scores outside the 1–5 range."""
        for field in fields(self):
            score = getattr(self, field.name)

            # bool is a subclass of int in Python, so it must be rejected explicitly.
            if isinstance(score, bool) or not isinstance(score, int):
                raise TypeError(f"{field.name} must be an integer")

            if not MIN_SCORE <= score <= MAX_SCORE:
                raise ValueError(
                    f"{field.name} must be between {MIN_SCORE} and {MAX_SCORE}"
                )

    @property
    def overall_score(self) -> float:
        """Return the arithmetic mean of all rubric scores."""
        values = [getattr(self, field.name) for field in fields(self)]
        return round(sum(values) / len(values), 2)


@dataclass(frozen=True)
class Evaluation:
    """One human-readable evaluation of an AI response."""

    prompt: str
    response: str
    scores: EvaluationScores
    rationale: str

    def __post_init__(self) -> None:
        """Ensure the text fields contain meaningful non-whitespace content."""
        for name in ("prompt", "response", "rationale"):
            value = getattr(self, name)

            if not isinstance(value, str):
                raise TypeError(f"{name} must be a string")

            if not value.strip():
                raise ValueError(f"{name} cannot be empty")
