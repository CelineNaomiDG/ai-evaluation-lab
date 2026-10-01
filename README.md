# AI Evaluation Lab

[![CI](https://github.com/CelineNaomiDG/ai-evaluation-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/CelineNaomiDG/ai-evaluation-lab/actions/workflows/ci.yml)

A practical Python project for evaluating, comparing and tracking AI responses with an explicit, inspectable quality rubric.

> **Status:** In progress — working V1 foundation with automated tests, CI and a reproducible Docker runtime.

## Why this project exists

Teams building with LLMs need repeatable ways to answer questions such as:

- Did a prompt change improve or regress output quality?
- Which responses fail repeatedly, and why?
- Are outputs correct, factual, relevant and complete?
- Can human and automated evaluations be compared consistently?

AI Evaluation Lab turns qualitative review into structured evaluation data instead of relying on a vague "looks good" judgement.

## Demonstrated engineering work

The current project includes:

- typed Python data models for evaluations and rubric scores;
- explicit input validation and edge-case handling;
- deterministic overall-score calculation;
- JSON persistence and round-trip loading;
- unit and parameterized tests with `pytest`;
- an executable example workflow;
- GitHub Actions CI across Python 3.11, 3.12 and 3.13;
- a Dockerfile for a reproducible runtime;
- project documentation and a transparent roadmap.

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

## Repository structure

```text
ai-evaluation-lab/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── ai_evaluation_lab/
│       ├── __init__.py
│       ├── evaluator.py
│       └── storage.py
├── tests/
│   ├── test_evaluator.py
│   └── test_storage.py
├── examples/
│   └── basic_evaluation.py
├── docs/
│   └── rubric.md
├── data/
│   └── .gitkeep
├── Dockerfile
├── .dockerignore
├── pyproject.toml
└── README.md
```

## Run locally

Requires Python 3.11+.

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python examples/basic_evaluation.py
```

The example writes an evaluation result to `data/example_evaluation.json`.

## Run with Docker

```bash
docker build -t ai-evaluation-lab .
docker run --rm ai-evaluation-lab
```

## Roadmap

### V1 — Python evaluation core
- [x] Evaluation model and input validation
- [x] Rubric scoring
- [x] Overall score calculation
- [x] JSON persistence
- [x] Unit and edge-case tests
- [x] Runnable example
- [x] GitHub Actions CI
- [x] Docker runtime

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
- [ ] Deployment
- [ ] Logging and monitoring
- [ ] Authentication / authorization
- [ ] Security review

## Technical focus

**Implemented:** Python · OOP/data modelling · type hints · pytest · JSON · Git/GitHub · GitHub Actions · Docker

**Planned expansion:** FastAPI · PostgreSQL · LLM APIs · deployment · monitoring

## Development approach

**Build → test → document → improve.**

The repository intentionally distinguishes completed work from planned work so that the technical evidence remains easy to verify.

## Author

**Celine de Graaf**  
Bachelor Informatica — Open Universiteit — In Progress  
[GitHub profile](https://github.com/CelineNaomiDG) · [Portfolio](https://celine-portfolio-flame.vercel.app)
