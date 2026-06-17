# House Price Prediction using Linear Regression

## Problem Statement

HomeVista Properties operates across multiple cities and handles thousands of residential property sales every year. The company wants to automate its house pricing process using Machine Learning.

The objective of this project is to build a Linear Regression model that can predict the selling price of a house based on its physical features, location, and condition using historical property data.

---

## Dataset Features

- Id – Unique identification number
- MSSubClass – Type of dwelling involved in the sale
- MSZoning – General zoning classification
- LotArea – Lot size in square feet
- LotConfig – Lot configuration
- BldgType – Type of dwelling
- OverallCond – Overall condition rating
- YearBuilt – Original construction year
- YearRemodAdd – Year remodeled or additions made
- Exterior1st – Exterior covering on house
- BsmtFinSF2 – Type 2 finished basement area
- TotalBsmtSF – Total basement area
- SalePrice – Final selling price (Target Variable)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn

---

## Machine Learning Algorithm

- Linear Regression

---

## Steps Performed

1. Loaded the dataset using Pandas.
2. Converted categorical values into numerical values.
3. Removed the `Id` column.
4. Split the dataset into training and testing sets.
5. Trained a Linear Regression model.
6. Predicted house prices.
7. Evaluated the model using MAE, MSE, RMSE, and R² Score.

---

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Repository Structure

```
AssignmentProject/
│
├── code.py
├── HousePricePrediction.csv
└── README.md
```

---

## How to Run

```bash
python code.py
```

---

## Author

Aniruddha Ahir