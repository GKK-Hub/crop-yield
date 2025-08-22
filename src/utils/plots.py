"""
plots.py

Provides helper functions for visualizing regression model performance.
Currently includes:

- Actual vs. Predicted plot
- Residuals vs. Predicted plot

These plots help in visually assessing how well the model fits the data
and detecting bias, variance, or systematic errors.
"""

# Prediction Error Display
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import PredictionErrorDisplay
from sklearn.model_selection import ValidationCurveDisplay
from sklearn.pipeline import Pipeline

def prediction_error_display(y_test: np.ndarray, y_pred: np.ndarray):
  ''' Displays the actual vs predicted values and residual vs predicted values'''

  plt.style.use('fivethirtyeight')

  fig, axs = plt.subplots(ncols=2, figsize=(14, 8))
  PredictionErrorDisplay.from_predictions(
      y_test,
      y_pred=y_pred,
      kind="actual_vs_predicted",
      ax=axs[0],
  )
  axs[0].set_title("Actual vs. Predicted values")
  PredictionErrorDisplay.from_predictions(
      y_test,
      y_pred=y_pred,
      kind="residual_vs_predicted",
      ax=axs[1],
  )
  axs[1].set_title("Residuals vs. Predicted Values")
  # fig.suptitle(plot_title)
#   plt.tight_layout()
#   plt.show()
  return fig

def validation_curve_display(estimator:Pipeline,
                             X:pd.DataFrame, 
                             y:pd.Series, 
                             param_name: str, 
                             param_range: list, 
                             cv, 
                             scoring:str, 
                             negate_score:bool = True):
  ''' Displays the Validation Curve for a hyperparameter '''

  plt.style.use('fivethirtyeight')

  fig, axs = plt.subplots(figsize=(14, 8))
  ValidationCurveDisplay.from_estimator(estimator=estimator, 
                                        X=X,
                                        y=y,
                                        param_name=param_name,
                                        param_range=param_range,
                                        cv=cv,
                                        scoring=scoring,
                                        negate_score=negate_score,
                                        ax=axs)
  axs.set_title(f'Validations Curve for {param_name}')
  return fig


