# ShopSmart – Online Shoppers Purchase Prediction

## Problem Statement

An e-commerce company, **ShopSmart**, wants to better understand the behaviour of visitors browsing its online store.

Every day, thousands of users navigate through product pages, spend varying amounts of time on the website, and interact differently with content. Currently, the company is unable to accurately predict which visitors are likely to complete a purchase, resulting in inefficient marketing strategies and lost revenue opportunities.

To address this challenge, the company has collected data over a period of one year. Each session represents a unique visitor session to ensure unbiased insights, avoiding the influence of specific users, promotional campaigns, seasonal trends, or special events.

The dataset contains **12,330 individual user sessions** and includes a mix of **numerical and categorical features** that capture detailed information about users' browsing behaviour and interactions with the website.

As a **Machine Learning Engineer**, you are required to build a predictive model that can determine whether a visitor is likely to make a purchase based on their session behaviour.

Your task involves:

- Performing **Exploratory Data Analysis (EDA)**.
- Applying appropriate **feature preprocessing and transformations**.
- Developing a **Decision Tree–based classification model**.
- Handling the **imbalanced nature of the dataset**.
- Evaluating model performance using the **F1-score** metric.

## Objective

Develop a machine learning model capable of predicting whether a website visitor will complete a purchase during a session.

The primary goal is to maximize the **F1-score**, with a benchmark value of **0.55** used to assess the effectiveness of the solution.

> **Note:** Use **pruning techniques** to improve the performance and generalization ability of the `DecisionTreeClassifier`.

---

# Dataset Description

- **Total Records:** 12,330 user sessions
- **Observation Unit:** Individual website session
- **Target Variable:** Revenue
- **Problem Type:** Binary Classification

---

## Features Description

| Feature Name | Description |
|-------------|-------------|
| `Administrative` | Number of pages visited related to account management (login, profile, settings, etc.) |
| `Administrative_Duration` | Total time (in seconds) spent on administrative pages |
| `Informational` | Number of informational pages visited (FAQs, policies, help pages, etc.) |
| `Informational_Duration` | Total time (in seconds) spent on informational pages |
| `ProductRelated` | Number of product-related pages visited |
| `ProductRelated_Duration` | Total time (in seconds) spent on product-related pages |
| `BounceRates` | Percentage of visitors who leave the website after viewing only one page |
| `ExitRates` | Percentage of exits from a particular page |
| `PageValues` | Average value of pages visited before completing a transaction |
| `SpecialDay` | Closeness of the visit date to a special day (e.g., Valentine's Day, Mother's Day) |
| `Month` | Month during which the visit occurred (Feb, Mar, May, etc.) |
| `OperatingSystems` | Operating system used by the visitor (encoded) |
| `Browser` | Browser used by the visitor (encoded) |
| `Region` | Geographic region of the visitor (encoded) |
| `TrafficType` | Source of website traffic (direct, referral, advertisements, etc.) |
| `VisitorType` | Type of visitor (`Returning_Visitor`, `New_Visitor`, `Other`) |
| `Weekend` | Indicates whether the session occurred on a weekend |
| `Revenue` | Indicates whether the visitor completed a purchase (**Target Variable**) |

---

# Expected Workflow

## 1. Exploratory Data Analysis (EDA)

- Understand the dataset structure.
- Identify missing values and duplicates.
- Analyze class distribution.
- Explore relationships between features and the target variable.
- Visualize important patterns and trends.

---

## 2. Data Preprocessing

- Handle missing values (if any).
- Encode categorical variables.
- Transform features where necessary.
- Prepare the dataset for modeling.
- Address class imbalance using suitable techniques.

---

## 3. Model Development

Build a classification model using:

- `DecisionTreeClassifier`

Apply pruning techniques such as:

- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- `ccp_alpha` (Cost Complexity Pruning)

to improve model performance and reduce overfitting.

---

## 4. Model Evaluation

Evaluate the model using the following metrics:

- F1-Score (**Primary Metric**)
- Accuracy
- Precision
- Recall
- Confusion Matrix
- Classification Report

### Benchmark

- **Target F1-Score:** `≥ 0.55`

---

# Deliverables

- Exploratory Data Analysis (EDA)
- Data preprocessing pipeline
- Decision Tree classification model
- Pruning implementation
- Model evaluation results
- Final insights and conclusions

---

# Conclusion

By leveraging user browsing behaviour data, ShopSmart aims to accurately identify visitors with a high likelihood of making a purchase. A well-optimized Decision Tree model with appropriate preprocessing and pruning can help the company improve marketing strategies, personalize customer experiences, and increase revenue opportunities.