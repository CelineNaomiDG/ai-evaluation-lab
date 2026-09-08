import pytest

from ai_evaluation_lab.evaluator import Evaluation, EvaluationScores


def valid_scores(**overrides: int) -> EvaluationScores:
    values = {
        "correctness": 4,
        "factuality": 4,
        "instruction_following": 4,
        "relevance": 4,
        "completeness": 4,
        "clarity": 4,
        "safety": 4,
    }
    values.update(overrides)
    return EvaluationScores(**values)


def test_overall_score_is_average_of_all_criteria() -> None:
    scores = EvaluationScores(
        correctness=5,
        factuality=4,
        instruction_following=3,
        relevance=5,
        completeness=4,
        clarity=5,
        safety=5,
    )

    assert scores.overall_score == 4.43


@pytest.mark.parametrize("invalid_score", [0, 6, -1, 100])
def test_score_outside_range_is_rejected(invalid_score: int) -> None:
    with pytest.raises(ValueError):
        valid_scores(correctness=invalid_score)


@pytest.mark.parametrize("invalid_score", [4.5, "5", None, True])
def test_non_integer_score_is_rejected(invalid_score: object) -> None:
    with pytest.raises(TypeError):
        valid_scores(correctness=invalid_score)  # type: ignore[arg-type]


@pytest.mark.parametrize("field_name", ["prompt", "response", "rationale"])
def test_empty_evaluation_text_is_rejected(field_name: str) -> None:
    values = {
        "prompt": "Explain HTTP status code 404.",
        "response": "404 means that the requested resource was not found.",
        "scores": valid_scores(),
        "rationale": "The response is correct, relevant and concise.",
    }
    values[field_name] = "   "

    with pytest.raises(ValueError):
        Evaluation(**values)  # type: ignore[arg-type]


def test_valid_evaluation_is_created() -> None:
    evaluation = Evaluation(
        prompt="Explain HTTP status code 404.",
        response="404 means that the requested resource was not found.",
        scores=valid_scores(correctness=5, factuality=5),
        rationale="The answer is factually correct and directly answers the prompt.",
    )

    assert evaluation.prompt.startswith("Explain")
    assert evaluation.scores.overall_score == 4.29
