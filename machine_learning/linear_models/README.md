# Linear Models

Machine learning project on linear models, regularization and model
interpretability, built with Scikit-learn.

## Requirements

- Ubuntu 20.04 LTS, python3 version 3.11
- Every file starts with the python3 shebang and ends with a new line
- Every file is executable
- Code follows pycodestyle 2.14.0
- Every module, class and function carries a docstring

## The dataset

A custom-built dataset is used from Task 0 to Task 2 and in Task 4. X2 is
almost a copy of X1, and the target is built from X1 and X3 only. That
multicollinearity is deliberate: ordinary least squares cannot tell X1 and X2
apart and splits the weight between them in an unstable way, which is the
problem regularization exists to solve.

## Tasks

| File | Task |
|---|---|
| 0-linear_regression.py | Build an untrained LinearRegression model |

## Author

Kleant Laboti
