import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, Lasso, Ridge
from sklearn.metrics import accuracy_score, precision_score

df = pd.read_csv("employee_turnover.csv")

X = df.drop("Employee_Turnover", axis=1)
y = df["Employee_Turnover"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

baseline = LogisticRegression(max_iter=1000)
baseline.fit(X_train, y_train)

baseline_pred = baseline.predict(X_test)

print("Baseline Logistic Regression")
print("Accuracy:", accuracy_score(y_test, baseline_pred))
print("Precision:", precision_score(y_test, baseline_pred))

lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

lasso_pred = lasso.predict(X_test)
lasso_pred = (lasso_pred >= 0.5).astype(int)

print("\nLasso (L1)")
print("Accuracy:", accuracy_score(y_test, lasso_pred))
print("Precision:", precision_score(y_test, lasso_pred))

ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

ridge_pred = ridge.predict(X_test)
ridge_pred = (ridge_pred >= 0.5).astype(int)

print("\nRidge (L2)")
print("Accuracy:", accuracy_score(y_test, ridge_pred))
print("Precision:", precision_score(y_test, ridge_pred))