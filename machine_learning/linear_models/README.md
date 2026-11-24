# Linear Models

A Scikit-learn project on linear models: what happens when ordinary least
squares meets correlated features, how L1 and L2 regularization fix it in
different ways, how to read a model with SHAP, and where a linear decision
boundary stops being enough.

## Requirements

- Ubuntu 20.04 LTS, python3 version 3.11
- Every file begins with the python3 shebang and ends with a new line
- Every file is executable
- Code follows pycodestyle 2.14.0
- Every module and function carries a docstring

Packages: numpy 2.0.2, scikit-learn 1.6.1, shap 0.48.0, pillow 11.3.0

## The problem the project explores

The regression dataset is built so that X2 is almost a copy of X1, while the
target is generated from X1 and X3 only. Ordinary least squares cannot decide
which twin deserves the credit, so it splits the weight wildly.

| Model | X1 | X2 | X3 |
|---|---|---|---|
| True relationship | 4 | 0 | 3 |
| Linear regression | -5.08 | +9.10 | 3.08 |
| Ridge, alpha 1.0 | 1.05 | 2.98 | 3.08 |

The linear model still predicts well, since the two coefficients sum to about
4.03. What is broken is the interpretation. That gap between predicting well
and explaining honestly is the thread running through all seven tasks.

## Tasks

| File | Function | What it does |
|---|---|---|
| 0-linear_regression.py | Linear_Regression() | Untrained LinearRegression |
| 1-regression_evaluation_metrics.py | evaluation_metrics_for_regression() | Returns MSE, RMSE, MAE, R squared |
| 2-ridge_regression.py | ridge_regression() | Untrained Ridge, L2 penalty |
| 3-Lasso_regression.py | lasso_regression() | Untrained Lasso, L1 penalty |
| 4-shap.py | get_shap_explainer_and_values() | SHAP explainer and values |
| 5-logisitc_regression.py | Logistic_Regression_Model() | Untrained LogisticRegression |
| 6-svm.py | get_SVM_model() | SVC with linear, poly or rbf kernel |

## Results

Regression on the multicollinear dataset:

| Model | R squared |
|---|---|
| Linear | 0.8266 |
| Ridge | 0.8310 |

Regression on the 50-feature dataset where only 5 features matter:

| Model | R squared | Features used |
|---|---|---|
| Linear | 0.4885 | 50 of 50 |
| Lasso | 0.8185 | 6 of 50 |

Classification on three concentric rings:

| Model | Accuracy |
|---|---|
| Logistic regression | 0.27 |
| SVM linear | 0.37 |
| SVM poly | 0.45 |
| SVM RBF | 0.95 |

## What the project demonstrates

Good prediction and good interpretation are different goals. Ridge barely
changed R squared while fixing the coefficients completely.

L1 and L2 solve different problems. Ridge shrinks correlated coefficients
toward each other and keeps every feature. Lasso drives weak coefficients to
exactly zero and performs feature selection.

More features is not more information. With 45 of 50 columns being noise, the
model that used all of them scored 0.49 against 0.82.

SHAP explains the model, not reality. It named X2 the most important feature
in both models, and X2 contributes nothing to the real target.

Match the model to the shape of the data. Logistic regression is not weak, it
was simply the wrong tool for concentric rings.

## Naming traps

Three filenames are easy to get wrong and break the checker import.

| Expected | Common mistake |
|---|---|
| Linear_Regression | linear_regression |
| 3-Lasso_regression.py | lowercase L |
| 5-logisitc_regression.py | correct spelling of logistic |

The third is a genuine typo in the task main file and has to be reproduced.

## Author

Kleant Laboti
