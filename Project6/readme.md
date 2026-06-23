
## Project Title
**Health Risk Classification using Supervised Machine Learning**

## Problem Statement

A leading biomedical research institute, **NovaGen Research Labs**, is conducting large-scale population health studies to better understand how underlying health conditions influence disease risk and long-term health outcomes.

Every year, the institute recruits thousands of volunteers who undergo medical examinations, lifestyle assessments, and clinical tests. However, researchers currently lack a reliable way to consistently distinguish between individuals with generally **healthy profiles** and those who may be at **higher health risk**, limiting the effectiveness of participant selection and stratified analysis in their studies.

To address this challenge, the institute has compiled a dataset consisting of health records collected over multiple observational studies. Each record represents a unique participant to avoid sampling bias and ensure independent observations.

The dataset includes a combination of numerical and categorical health indicators, such as physiological measurements, lifestyle factors, and medical history attributes, providing a comprehensive view of each individual's health status.

As a **Data Scientist**, your task is to develop a predictive model that classifies individuals as either **Healthy** or **Unhealthy** based on the available health data.

This classification will support key research decisions, including:

- Selecting eligible participants for clinical trials and longitudinal studies.
- Stratifying populations for risk-based analysis and outcome comparison.
- Improving participant screening efficiency.
- Supporting data-driven healthcare research initiatives.

---

## Dataset Overview

- **Total Records:** 9,800 individuals
- **Observation Type:** Each record represents one unique participant.
- **Problem Type:** Supervised Machine Learning (Binary Classification)
- **Target Variable:** Health outcome/risk classification.

---

## Dataset Features

| Feature Name | Description |
|-------------|-------------|
| Age | Age of the individual (in years) |
| BMI | Body Mass Index, measuring body fat based on height and weight |
| Blood_Pressure | Systolic blood pressure (mmHg) |
| Cholesterol | Cholesterol level (mg/dL) |
| Glucose_Level | Blood glucose level (mg/dL) |
| Heart_Rate | Resting heart rate (beats per minute) |
| Sleep_Hours | Average number of sleep hours per day |
| Exercise_Hours | Average hours of exercise per day |
| Water_Intake | Daily water intake (litres) |
| Stress_Level | Stress level on a predefined scale (e.g., 1–10) |
| Smoking | Smoking habit (1 = Smoker, 0 = Non-smoker) |
| Alcohol | Alcohol consumption (1 = Yes, 0 = No) |
| Diet | General diet category encoded numerically |
| MentalHealth | Mental health score or condition indicator |
| PhysicalActivity | Overall physical activity level |
| MedicalHistory | Presence of prior medical conditions |
| Allergies | Presence of known allergies |
| Diet_Type__Vegan | One-hot encoded: 1 if diet is Vegan |
| Diet_Type__Vegetarian | One-hot encoded: 1 if diet is Vegetarian |
| Blood_Group_AB | One-hot encoded: Blood group AB |
| Blood_Group_B | One-hot encoded: Blood group B |
| Blood_Group_O | One-hot encoded: Blood group O |

---

## Target Variable

| Variable | Description |
|----------|-------------|
| Target | Health outcome classification representing the individual's health status or risk level |

### Class Labels

- **0 → Healthy**
- **1 → Unhealthy**

> *Use the actual encoding from the dataset if it differs.*

---

## Objective

Build and evaluate a supervised machine learning model capable of accurately predicting whether an individual is **Healthy** or **Unhealthy** using the provided health indicators.

---

## Project Workflow

1. Data Loading and Exploration
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Hyperparameter Tuning
9. Final Model Selection
10. Prediction and Interpretation

---

## Suggested Machine Learning Models

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Gradient Boosting
- XGBoost
- AdaBoost

---

## Evaluation Metrics

Since this is a binary classification problem, the following metrics can be used:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

---

## Expected Outcome

The final model should effectively classify participants into **Healthy** and **Unhealthy** categories, enabling NovaGen Research Labs to:

- Improve participant selection for studies.
- Conduct risk-based population analysis.
- Enhance the quality of biomedical research.
- Support evidence-based healthcare decision-making.

---

## Author
Aniruddha Ahir
- **Project Type:** Binary Classification
- **Dataset Size:** 9,800 Health Records
- **Domain:** Healthcare / Biomedical Research

---

### README Summary

Develop a supervised machine learning model that predicts whether an individual is healthy or unhealthy using demographic, lifestyle, physiological, and medical history data collected from 9,800 participants.