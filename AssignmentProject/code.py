import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("HousePricePrediction.csv")

df["MSZoning"] = df["MSZoning"].replace({"RL": 0, "RM": 1, "FV": 2})
df["LotConfig"] = df["LotConfig"].replace({"Inside": 0, "Corner": 1, "CulDSac": 2})
df["BldgType"] = df["BldgType"].replace({"1Fam": 0, "2fmCon": 1, "Duplex": 2})
df["Exterior1st"] = df["Exterior1st"].replace({"VinylSd": 0, "MetalSd": 1, "Wd Sdng": 2, "HdBoard": 3, "BrkFace": 4})

df = df.drop("Id", axis=1)

X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predicted Prices:")
print(y_pred[:5])

print("\nActual Prices:")
print(y_test.values[:5])

print("\nMAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))