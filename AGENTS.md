# AI Agent Guidance for this Repository

## Purpose
This repository contains a small Python-focused analysis project with a Jupyter notebook and a simple plotting script. These instructions help AI coding agents understand the repo layout and avoid assumptions about missing project metadata.

## Repository structure
- `Joker_Analysis.ipynb` – main Jupyter notebook for Joker lottery data analysis
- `test.py` – simple Python script demonstrating a matplotlib pie chart

## Key points for agents
- There is no `requirements.txt`, `setup.py`, `pyproject.toml`, or test harness in this repo.
- Use Python and Jupyter notebook conventions.
- The notebook imports `pandas`, `matplotlib.pyplot`, and `seaborn`.
- The notebook currently loads the dataset from an absolute Windows path: `c:\Dev\Python\Datasets\Joker.csv`.
  - Do not assume the dataset exists in the repository.
  - If dataset access is required, ask the user whether to update the path or provide the data.

## Editing guidance
- Preserve existing notebook structure and markdown explanations when updating `Joker_Analysis.ipynb`.
- Prefer adding new analysis or visualization cells rather than merging everything into a single cell.
- Keep `test.py` simple and consistent with the current plotting style.

## When in doubt
- Ask the user before changing external data paths or adding new package dependencies.
- If a new dependency is needed, explain it clearly and keep the repo minimal.
