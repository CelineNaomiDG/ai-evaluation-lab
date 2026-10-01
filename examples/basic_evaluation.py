from pathlib import Path

from ai_evaluation_lab import Evaluation, EvaluationScores
from ai_evaluation_lab.storage import save_evaluation


def main() -> None:
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

    output_path = save_evaluation(
        evaluation,
        Path("data/example_evaluation.json"),
    )
    print(
        f"Saved evaluation with overall score "
        f"{evaluation.scores.overall_score} to {output_path}"
    )


if __name__ == "__main__":
    main()
