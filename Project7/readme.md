# SmartCart Customer Clustering System

## Problem Statement

**SmartCart** is a growing e-commerce platform serving customers across multiple countries. The company has collected extensive customer data consisting of **2,240 customer records** and **22 attributes**, including demographics, purchase behavior, website activity, and customer responses.

Currently, SmartCart uses **generic marketing and engagement strategies** for all customers without clearly understanding different customer behavior patterns. This results in:

* Inefficient marketing campaigns
* Missed opportunities to retain high-value customers
* Delayed identification of churn-prone customers
* Poor customer personalization
* Reduced customer engagement and loyalty

To address these challenges, SmartCart aims to build an **Intelligent Customer Segmentation System** using **Unsupervised Machine Learning**.

The system will analyze historical customer transaction data and automatically group customers into meaningful clusters based on:

* Purchasing behavior
* Engagement levels
* Loyalty indicators
* Spending patterns
* Website activity

As an **AI/ML Engineer**, your task is to develop this system using **clustering algorithms** to discover hidden patterns in customer behavior and support **data-driven decision-making**, personalized marketing, and customer retention strategies.

---

# Dataset Description

Each row in the dataset represents a **single customer** and contains multiple attributes describing their demographics, spending habits, purchasing behavior, and engagement with the SmartCart platform.

---

## 1. Customer Demographics

| Feature        | Description                                |
| -------------- | ------------------------------------------ |
| ID             | Unique customer identifier                 |
| Year_Birth     | Year of birth of the customer              |
| Education      | Highest education level achieved           |
| Marital_Status | Marital status of the customer             |
| Income         | Yearly household income                    |
| Kidhome        | Number of small children in the household  |
| Teenhome       | Number of teenagers in the household       |
| Dt_Customer    | Date when customer enrolled with SmartCart |

---

## 2. Purchase Behavior (Amount Spent)

| Feature          | Description                    |
| ---------------- | ------------------------------ |
| MntWines         | Amount spent on wine products  |
| MntFruits        | Amount spent on fruits         |
| MntMeatProducts  | Amount spent on meat products  |
| MntFishProducts  | Amount spent on fish products  |
| MntSweetProducts | Amount spent on sweet products |
| MntGoldProds     | Amount spent on gold products  |

---

## 3. Purchase Behavior (Frequency)

| Feature             | Description                             |
| ------------------- | --------------------------------------- |
| NumDealsPurchases   | Purchases made using discounts or deals |
| NumWebPurchases     | Purchases made through the website      |
| NumCatalogPurchases | Purchases made through catalogs         |
| NumStorePurchases   | Purchases made in physical stores       |
| NumWebVisitsMonth   | Number of website visits per month      |

---

## 4. Customer Feedback & Loyalty Indicators

| Feature  | Description                                                           |
| -------- | --------------------------------------------------------------------- |
| Recency  | Number of days since the last purchase                                |
| Complain | Whether the customer complained in the last 2 years (1 = Yes, 0 = No) |

---

# Project Objective

Build an AI-powered customer segmentation system that:

1. Performs data preprocessing and feature engineering.
2. Applies clustering algorithms such as:

   * K-Means Clustering
   * Hierarchical Clustering
   * DBSCAN (optional)
3. Identifies meaningful customer segments.
4. Visualizes customer clusters.
5. Provides actionable business insights.
6. Enables personalized marketing campaigns.
7. Improves customer retention and engagement.

---

# Expected Outcomes

After clustering, SmartCart should be able to identify customer groups such as:

* High-Value Loyal Customers
* Frequent Online Shoppers
* Discount-Oriented Customers
* Inactive or Churn-Risk Customers
* Premium Product Buyers
* Low-Spending Customers

These insights will help SmartCart optimize marketing efforts, improve customer satisfaction, and increase overall revenue.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

# Machine Learning Approach

**Type:** Unsupervised Learning

**Algorithms:**

* K-Means Clustering
* Hierarchical Clustering
* DBSCAN (Optional)

**Evaluation Techniques:**

* Elbow Method
* Silhouette Score
* Cluster Visualization
* Business Interpretation of Clusters

---

# Business Impact

The SmartCart Customer Clustering System will help:

* Improve marketing efficiency
* Increase customer retention
* Enable personalized recommendations
* Identify high-value customers
* Detect potential churn risks
* Support data-driven business decisions
