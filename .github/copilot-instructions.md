# GitHub Copilot Instructions

This repository contains a small Python data analysis notebook and a simple plotting script.

## Important notes for Copilot
- Use Python and Jupyter notebook conventions for edits.
- The notebook imports `pandas`, `matplotlib.pyplot`, and `seaborn`.
- The notebook currently loads data from an absolute Windows path: `c:\Dev\Python\Datasets\Joker.csv`.
  - Do not assume the dataset is present in the repository.
  - Ask the user before changing the file path or adding new data files.

## Editing guidance
- Preserve existing notebook structure and markdown commentary in `Joker_Analysis.ipynb`.
- Use headings of various levels that separate and clearly demarcate the various sections.
- Prefer adding new notebook cells for additional analysis or visualization.
- Keep `test.py` simple and consistent with its existing matplotlib pie chart example.
- Do not introduce unnecessary dependencies.

## When you need clarification
- Ask the user if the dataset should be moved into the repository or if a relative path should be used.
- Ask the user before creating new Python packaging or test files.
