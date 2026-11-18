# Contributing to Forma

Thanks for your interest. This guide covers setup, the checks CI runs, and the workflow for
a change. The README links here for contribution guidelines.

## Setup

```sh
git clone https://github.com/zachshallbetter/forma.git
cd forma
python -m venv forma_env
source forma_env/bin/activate      # Windows: forma_env\Scripts\activate
pip install -r requirements.txt
pip install .
```

`setup.py` requires Python 3.7 or later. GPU acceleration needs a CUDA-capable NVIDIA GPU
(see the README's system requirements). `docs/developer_guide.md` describes the project
structure and coding guidelines in more detail.

## Verifying a change

CI (`.github/workflows/python-app.yml`) runs these on every push and pull request to
`main`. Run them before opening a PR:

```sh
python -m unittest discover tests
pip install flake8 black
flake8 .
black --check .
```

The tests in `tests/` are unit tests, one module per pipeline stage plus a workflow test.

## Conventions

- Source lives under `src/`, one package per pipeline stage (`preprocessing`, `calibration`,
  `reconstruction`, and so on); tests mirror them as `tests/test_<stage>.py`.
- Code must pass `flake8` and `black --check`.
- Recent history mixes plain and conventional commit messages (`feat: ...`). Prefer the
  conventional form: `feat: ...`, `fix: ...`, `docs: ...`, `test: ...`, `chore: ...`.
- Keep README claims to what the code and tests support.

## Pull requests

- Branch off `main`; keep PRs focused.
- Describe the change and how you verified it. The PR template prompts for this.
- Participation is covered by the [Code of Conduct](CODE_OF_CONDUCT.md).
