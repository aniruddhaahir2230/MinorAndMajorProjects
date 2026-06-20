# Iris Flower Species Classification using Supervised Machine Learning

## Project Overview

This project aims to build a Machine Learning-based classification system that can automatically identify the species of an Iris flower based on its physical measurements. Three supervised learning algorithms are trained and compared to determine the best-performing model.

## Problem Statement

A botanical research centre is studying different species of Iris flowers to automate the plant identification process.

Currently, botanists manually identify flower species by measuring sepal and petal dimensions, which is:

* Time-consuming
* Error-prone
* Not scalable

The goal is to develop a Machine Learning model that can accurately predict the species of an Iris flower using its measurements.

## Dataset Description

The Iris dataset contains 150 flower samples belonging to three different species.

| Feature       | Description                                  |
| ------------- | -------------------------------------------- |
| SepalLengthCm | Length of sepal (cm)                         |
| SepalWidthCm  | Width of sepal (cm)                          |
| PetalLengthCm | Length of petal (cm)                         |
| PetalWidthCm  | Width of petal (cm)                          |
| Species       | Iris-setosa, Iris-versicolor, Iris-virginica |

## Algorithms Used

* K-Nearest Neighbours (KNN)
* Logistic Regression
* Gaussian Naive Bayes

## Project Workflow

1. Load the Iris dataset
2. Perform data preprocessing
3. Split the dataset into training and testing sets
4. Train KNN, Logistic Regression, and Naive Bayes models
5. Evaluate model performance
6. Compare results
7. Select the best-performing model

## Evaluation Metrics

* Accuracy Score
* Precision Score
* Recall Score
* F1 Score

## Results

The performance of all three models is compared using the evaluation metrics mentioned above. The model with the highest overall performance is selected as the final classifier.

## Note

The Iris dataset is small, clean, and perfectly balanced, containing 150 samples equally distributed among three classes (50 samples each). Because of its simplicity, machine learning models often achieve very high accuracy on this dataset.

However, real-world datasets are usually:

* Imbalanced
* Noisy
* Incomplete
* More difficult to classify

To make the prediction task slightly more challenging, only 50% of the dataset is used for training, while the remaining 50% is used for testing.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

## Author

**Aniruddha Ahir**

