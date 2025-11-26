# DATA ANALYTIC

## Python - SQL

---

## Modules

### Week 7: Basic Python

- Tuesday:
  - Languages Overview: types, domain, implementation, supported paradigms.
  - Python: Introduction and installation.
  - Ways to run Python code.
  - Basic syntax and structure.
- Thursday:
  - Data types: int, float, string, boolean.
  - Lists, tuples, dictionaries, sets.
  - Control structures: if, for, while.
  - User-defined functions and modules.

### Week 8: Python + Data Connection

- Tuesday:
  - Environment management: packages and virtual environments.
  - Libraries for data analysis: pandas, numpy, matplotlib.
  - Reading and writing files: CSV, Excel.
- Thursday:
  - Requests to simple APIs.
  - SQL connection from Python.
  - Basic data manipulation: using Jypyter Notebook, matplotlib.

---

### Project Requirements

1. Install `Docker` [and (optional) `lazydocker`]
1. Install `uv`

---

### Navigation

You can focus on the following files/folders:

- `"Class Documents"/` folder - Contains lecture notes.
- `exercises/` folder - Contains exercises for practice.
- `README.md` - Project overview and instructions (this file).

---

### To run Exercises

NOTE: _replace `n` with the exercises set number_

```bash
uv run pytest _tests/test_exercises_n.py -vv
```

---

1. To run the project: `uv run main.py`
1. To run `Jupyter`:
   _(This is more convenient than `google colab` for connecting to the local database)_
   - `uv run jupyter JupyterNB.ipynb` (The notebook only)
   - `uv run jupyter lab JupyterNB.ipynb` (the full platform)
