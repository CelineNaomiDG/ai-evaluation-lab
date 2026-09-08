# AI Evaluation Lab

A practical LLM quality-assurance project for evaluating, comparing and tracking AI responses with a transparent rubric.

> **Status:** In Progress — v1 foundation

## Problem this project is solving

Teams building with LLMs need a repeatable way to answer questions such as:

- Did this new prompt make the output better or worse?
- Which model performs best for this task?
- Are responses becoming less factual, less complete or less safe?
- Which examples fail repeatedly and why?
- Can a human reviewer and an automated evaluator agree on quality?

A one-off "this answer looks good" judgement is difficult to compare over time. AI Evaluation Lab is being built to turn those reviews into structured, inspectable evaluation data.

The long-term product direction is a lightweight **LLM QA Bench**: upload or generate test cases, score outputs against a rubric, compare prompt/model versions and detect quality regressions before an AI feature is shipped.

## Current V1

The first version intentionally starts small and auditable. It will:

- represent an AI response evaluation as structured data;
- score responses against a fixed rubric;
- validate invalid or out-of-range inputs;
- calculate an overall score;
- persist evaluation results to JSON;
- include unit and edge-case tests with `pytest`;
- document design decisions and known limitations.

## Evaluation rubric

Each criterion is scored from **1 to 5**:

| Criterion | What it measures |
| --- | --- |
| Correctness | Whether the answer is logically and substantively correct |
| Factuality | Whether factual claims are accurate and supported |
| Instruction following | Whether the response follows the user's instructions |
| Relevance | Whether the response stays focused on the request |
| Completeness | Whether important parts of the request are addressed |
| Clarity | Whether the answer is understandable and well structured |
| Safety | Whether the response avoids unsafe or inappropriate behavior |

The rubric is intentionally explicit so evaluations can be inspected instead of relying on a vague "good/bad" label.

## Repository structure

```text
ai-evaluation-lab/
├── src/
│   └── ai_evaluation_lab/
│       ├── __init__.py
│       ├── evaluator.py
│       └── storage.py
├── tests/
│   ├── test_evaluator.py
│   └── test_storage.py
├── data/
│   └── .gitkeep
├── docs/
│   └── rubric.md
├── examples/
│   └── basic_evaluation.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Roadmap

### V1 — Python evaluation core
- [x] Evaluation model and input validation
- [x] Rubric scoring
- [x] Overall score calculation
- [ ] JSON persistence
- [x] Unit and edge-case tests for evaluator
- [ ] Example evaluation

### V2 — useful QA workflow
- [ ] Evaluation datasets / test cases
- [ ] Compare prompt or model versions
- [ ] Failure tags and regression summaries
- [ ] FastAPI endpoints
- [ ] PostgreSQL persistence
- [ ] API validation and tests

### V3 — LLM-assisted evaluation
- [ ] LLM provider integration
- [ ] Versioned evaluator prompts
- [ ] Human vs model evaluation comparison
- [ ] Evaluation metrics and agreement analysis

### V4 — production-oriented evidence
- [ ] Docker
- [ ] GitHub Actions CI
- [ ] Deployment
- [ ] Logging and monitoring
- [ ] Authentication / authorization
- [ ] Security review

## Learning goals

This project is being used to practice and demonstrate:

`Python` · `OOP` · `type hints` · `debugging` · `pytest` · `JSON` · `AI evaluation` · `Git/GitHub`

Later versions will add:

`FastAPI` · `PostgreSQL` · `LLM APIs` · `Docker` · `CI/CD` · `Azure` · `monitoring`

## Development approach

**Learn → build → commit → test → document → improve.**

AI coding tools may be used as pair-programming support, but each implementation should be understood, tested and explainable.

## Author

**Celine de Graaf**  
Bachelor Informatica — Open Universiteit — In Progress  
[GitHub profile](https://github.com/CelineNaomiDG)
