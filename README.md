# AI Evaluation Lab

A learning-focused Python project for evaluating AI responses with a transparent, reproducible rubric.

> **Status:** In Progress — v1 foundation

## Why this project exists

AI Evaluation Lab is being built as practical evidence for AI evaluation, software quality and Python development. The goal is not to hide the learning process: the repository will show how the evaluator evolves through small features, tests, bug fixes and documentation.

## V1 scope

The first version will:

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

## Planned repository structure

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
├── .gitignore
├── pyproject.toml
└── README.md
```

## Roadmap

### V1 — Python evaluation core
- [ ] Evaluation model and input validation
- [ ] Rubric scoring
- [ ] Overall score calculation
- [ ] JSON persistence
- [ ] Unit and edge-case tests
- [ ] Example evaluation

### V2 — API + database
- [ ] FastAPI endpoints
- [ ] PostgreSQL persistence
- [ ] API validation and tests

### V3 — LLM-assisted evaluation
- [ ] LLM provider integration
- [ ] Versioned prompts
- [ ] Human vs model evaluation comparison
- [ ] Evaluation dataset and metrics

### V4 — production-oriented evidence
- [ ] Docker
- [ ] GitHub Actions CI
- [ ] Deployment
- [ ] Logging and monitoring
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
