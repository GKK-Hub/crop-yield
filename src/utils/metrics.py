"""
metrics.py

Provides custom regression metrics and scoring functions for model evaluation.

Includes:
- Root Mean Squared Error (RMSE) function
- RMSE scorer for use with sklearn's GridSearchCV and cross-validation
- Regression summary printer with key metrics:
  Median Absolute Error, RMSE, RMSLE, R², and Adjusted R²

These functions standardize evaluation across models and enable consistent
reporting of model performance.
"""

# Custom Score
import numpy as np
from sklearn.metrics import make_scorer

# ------------------------------------------------------------------------------------

def rmse(actual: list, predict: list) -> float:
  '''Returns the Root Mean Squared Error (RMSE) given actual and predicted values'''

  # Converting list into a numpy array to make use of element-wise operations
  predict_array = np.array(predict)
  actual_array = np.array(actual)

  error = predict_array - actual_array

  squared_error = error ** 2
  mean_squared_error = squared_error.mean()
  rmse = np.sqrt(mean_squared_error)
  return rmse

rmse_score = make_scorer(rmse,  greater_is_better=False)

# ---------------------------------------------------------------------------------

# Regression Metrics
import sklearn.metrics as metrics
import numpy as np

def results(y_true: np.ndarray, y_predict: np.ndarray) -> None:
  '''Calculates different regression metrics and prints it'''

  mse = metrics.mean_squared_error(y_true, y_predict)
  med_abs_err = metrics.median_absolute_error(y_true, y_predict)
  rmsle = metrics.root_mean_squared_log_error(y_true, y_predict)
  rmse = np.sqrt(mse)
  r2 = metrics.r2_score(y_true, y_predict)

  print(f'Median Absolute Error: {round(med_abs_err, 2)}')
  print(f'Root Mean Squared Log Error: {round(rmsle, 2)}')
  print(f'Root Mean Squared Error: {round(rmse, 2)}')
  print(f'R^2: {round(r2, 2)}')
