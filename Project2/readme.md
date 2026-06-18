# Employee Turnover Prediction using Logistic Regression, Lasso, and Ridge

## Objective

The goal of this project is to predict whether an employee is likely to leave the company based on various employee-related factors. This helps organizations identify employees at risk of leaving and take proactive measures to improve retention.

## Models Used

### 1. Baseline Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for classification problems. It predicts the probability of an employee leaving the organization based on input features. This model serves as the baseline for comparison.

### 2. Lasso Regression (L1 Regularization)

Lasso Regression uses L1 regularization, which adds a penalty to the absolute values of model coefficients. This helps reduce overfitting and can automatically remove less important features by shrinking some coefficients to zero.

**Advantages:**

* Performs feature selection automatically.
* Reduces model complexity.
* Helps prevent overfitting.

### 3. Ridge Regression (L2 Regularization)

Ridge Regression uses L2 regularization, which adds a penalty to the squared values of model coefficients. Unlike Lasso, Ridge does not eliminate features but reduces the impact of less important features.

**Advantages:**

* Reduces overfitting.
* Handles multicollinearity effectively.
* Improves model stability.

## Regularization

Regularization is a technique used to prevent overfitting by penalizing large coefficient values.

### L1 Penalty (Lasso)

* Uses absolute values of coefficients.
* Can reduce some coefficients to zero.
* Useful for feature selection.

### L2 Penalty (Ridge)

* Uses squared values of coefficients.
* Shrinks coefficients toward zero.
* Keeps all features in the model.

## Evaluation Metrics

### Accuracy

Accuracy measures the proportion of correctly predicted instances out of all predictions.

**Formula:**

Accuracy = (Correct Predictions) / (Total Predictions)

### Precision

Precision measures how many of the employees predicted to leave actually left.

**Formula:**

Precision = True Positives / (True Positives + False Positives)

## Conclusion

Three models were implemented and compared:

1. Logistic Regression (Baseline)
2. Lasso Regression (L1)
3. Ridge Regression (L2)

The performance of each model was evaluated using Accuracy and Precision. The model with the best performance can be selected as the final model for predicting employee turnover.
