from ai_evaluation_lab.evaluator import Evaluation, EvaluationScores
from ai_evaluation_lab.storage import load_evaluation, save_evaluation


def test_evaluation_can_be_saved_and_loaded(tmp_path) -> None:
    evaluation = Evaluation(
        prompt="Explain HTTP status code 404.",
        response="404 means the requested resource was not found.",
        scores=EvaluationScores(
            correctness=5,
            factuality=5,
            instruction_following=5,
            relevance=5,
            completeness=4,
            clarity=5,
            safety=5,
        ),
        rationale="The response is correct, relevant and concise.",
    )

    output_file = tmp_path / "evaluation.json"
    saved_path = save_evaluation(evaluation, output_file)
    loaded = load_evaluation(saved_path)

    assert saved_path.exists()
    assert loaded["prompt"] == evaluation.prompt
    assert loaded["scores"]["correctness"] == 5
    assert loaded["overall_score"] == 4.86
