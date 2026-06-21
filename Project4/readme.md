# CreditWise Loan Approval System

## Project Overview

**CreditWise Loan Approval System** is a Machine Learning project developed for **SecureTrust Bank**, a mid-sized financial institution that provides personal and home loans across urban and rural regions of India.

The goal of this project is to automate the loan approval process by analyzing customer information and predicting whether a loan application should be **Approved** or **Rejected**. The system helps reduce manual effort, improve consistency, minimize bias, and speed up decision-making.

---

## Problem Statement

SecureTrust Bank currently relies on a manual loan verification process where loan officers evaluate applications using:

* Income proofs
* Employment details
* Credit history
* Existing loans
* Other financial documents

This traditional process is:

* Time-consuming
* Biased
* Inconsistent
* Difficult to scale

### Challenges Faced

#### 1. Good Customers Get Rejected

Some eligible applicants are rejected despite having a strong financial profile, resulting in loss of business opportunities.

#### 2. High-Risk Customers Get Approved

Some risky applicants are approved, increasing the probability of loan defaults and financial losses.

To solve these issues, SecureTrust Bank aims to implement an intelligent Machine Learning-based loan approval system that can predict loan approval decisions before final human verification.

---

## Objective

Develop a Machine Learning model that can:

* Analyze applicant information automatically
* Learn patterns from historical loan data
* Predict whether a loan should be approved or rejected
* Improve accuracy and consistency in loan approval decisions
* Reduce processing time and operational costs

---

## Dataset Description

Each record in the dataset represents a loan applicant and contains personal, financial, and credit-related information.

| Column Name        | Description                                  |
| ------------------ | -------------------------------------------- |
| Applicant_ID       | Unique applicant identifier                  |
| Applicant_Income   | Monthly income of applicant                  |
| Coapplicant_Income | Monthly income of co-applicant               |
| Employment_Status  | Salaried / Self-Employed / Business          |
| Age                | Applicant age                                |
| Marital_Status     | Married / Single                             |
| Dependents         | Number of dependents                         |
| Credit_Score       | Credit bureau score                          |
| Existing_Loans     | Number of currently active loans             |
| DTI_Ratio          | Debt-to-Income ratio                         |
| Savings            | Savings account balance                      |
| Collateral_Value   | Value of collateral provided                 |
| Loan_Amount        | Requested loan amount                        |
| Loan_Term          | Loan duration (months)                       |
| Loan_Purpose       | Home / Education / Personal / Business       |
| Property_Area      | Urban / Semi-Urban / Rural                   |
| Education_Level    | Undergraduate / Graduate / Postgraduate      |
| Gender             | Male / Female                                |
| Employer_Category  | Government / Private / Self-employed         |
| Loan_Approved      | Target Variable (1 = Approved, 0 = Rejected) |

---

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Loan Approval Prediction
8. Performance Optimization

---

## Expected Outcome

The system will analyze applicant details and predict loan approval status with high accuracy, helping the bank:

* Approve deserving customers faster
* Reduce loan default risks
* Eliminate manual bias
* Improve customer satisfaction
* Increase operational efficiency

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Jupyter Notebook

---

## Target Variable

**Loan_Approved**

* **1** → Loan Approved
* **0** → Loan Rejected

---

## Project Goal

Build an intelligent and reliable Machine Learning model that assists SecureTrust Bank in making faster, fairer, and more accurate loan approval decisions based on customer financial and personal information.
