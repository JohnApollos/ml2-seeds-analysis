# Seeds Dataset - ML2 Group Project

A machine learning analysis of the **UCI Seeds dataset** completed as part of **Machine Learning 2 coursework** in the **BSc Data Science and Analytics** program.

This project investigates whether geometric properties of wheat kernels can be used to distinguish among three wheat varieties: **Kama**, **Rosa**, and **Canadian**. The work combines **exploratory data analysis**, **unsupervised learning**, **supervised classification**, **hyperparameter tuning**, and **statistical model comparison**.

---

## Project Overview

The UCI Seeds dataset contains **210 wheat kernel samples**, each represented by **7 real-valued geometric features** extracted from soft X-ray images.

The main goal of this project is to evaluate how well machine learning methods can separate and classify the three wheat varieties, both with and without using the known labels.

This repository includes:

- exploratory data analysis
- clustering with K-Means and Hierarchical Clustering
- supervised learning with multiple classifiers
- hyperparameter tuning with `GridSearchCV` and `RandomizedSearchCV`
- model comparison using evaluation metrics and **McNemar's test**
- plots, notebooks, and saved result files

---

## Project Objectives

The project was designed around the following objectives:

- perform exploratory data analysis to understand feature distributions and class separability
- apply unsupervised learning techniques and compare recovered clusters against true labels
- train and evaluate multiple supervised classification models
- tune model hyperparameters for improved performance
- compare the best-performing models using McNemar's statistical significance test
- document findings clearly in report and presentation form

---

## Dataset Information

**Dataset:** Seeds
**Source:** UCI Machine Learning Repository
**Citation:** Charytanowicz, M., Niewczas, J., Kulczycki, P., Kowalski, P., & Lukasik, S. (2010). *Seeds* [Dataset]. UCI Machine Learning Repository.
**DOI:** https://doi.org/10.24432/C5H30K
**License:** CC BY 4.0

### Dataset Summary

| Property | Value |
|---|---|
| Number of instances | 210 |
| Number of features | 7 |
| Number of classes | 3 |
| Class labels | Kama, Rosa, Canadian |
| Missing values | None |
| Class balance | 70 samples per class |

### Features

The dataset contains the following input variables:

- area
- perimeter
- compactness
- kernel length
- kernel width
- asymmetry coefficient
- kernel groove length

---

## Methods Used

### 1. Exploratory Data Analysis

EDA was used to understand the structure of the dataset before modeling. This included:

- summary statistics
- class distribution checks
- correlation analysis
- pairwise feature visualization
- class-wise feature comparisons

### 2. Unsupervised Learning

Two clustering methods were applied:

- **K-Means Clustering**
- **Hierarchical Clustering** using Ward linkage

Cluster quality was evaluated against the true class labels using:

- **Adjusted Rand Index**
- **Normalized Mutual Information**
- **Silhouette Score**

### 3. Supervised Learning

The following classifiers were trained and evaluated:

- K-Nearest Neighbors
- Naive Bayes
- Decision Tree
- Logistic Regression
- Random Forest
- Support Vector Machine
- Gradient Boosting
- Multi-Layer Perceptron

### 4. Hyperparameter Tuning

Model optimization was performed using:

- `GridSearchCV`
- `RandomizedSearchCV`

### 5. Model Evaluation

Performance was assessed using:

- accuracy
- macro precision
- macro recall
- macro F1-score
- confusion matrices

### 6. Statistical Comparison

Top-performing models were compared using **McNemar's test** to determine whether differences in prediction performance were statistically significant.

---

## Repository Structure

```text
ml2-seeds-analysis/
│
├── data/                     # Dataset files
├── notebook/                 # Jupyter notebooks for analysis
├── plots/                    # Saved plots and visual outputs
├── results/                  # Exported results and evaluation outputs
├── run_supervised.py         # Script for supervised learning workflow
├── run_unsupervised.py       # Script for unsupervised learning workflow
├── requirements.txt          # Project dependencies
├── setup.sh                  # Environment setup script
├── test.sh                   # Project test script
└── README.md                 # Project documentation
```
## Setup and Installation
clone the repository and install dependencies

```bash
git clone https://github.com/JohnApollos/ml2-seeds-analysis.git
cd seeds-ml2-analysis
pip install -r requirements.txt
```
If needed, you can also use the helper scripts already included in the repository:
```
setup.sh
```
## Requirements
Main python libraries used in this project include:

```
ucimlrepo
pandas
numpy
scikit-learn
xgboost
matplotlib
seaborn
scipy
```
## Key Findings

The analysis showed that the Seeds dataset has strong internal structure and is well suited for both clustering and classification tasks.

### Main Findings

- The dataset is clean, balanced, and contains no missing values.
- Several geometric features are strongly correlated, especially size-related measurements.
- The three wheat varieties show meaningful separation in feature space.
- Hierarchical Clustering slightly outperformed K-Means in recovering the true class structure.
- Among the supervised models, Decision Tree and Random Forest were among the strongest performers.
- McNemar's test indicated that differences among the top models were not statistically significant on the selected test split.


## Team Members

| Member | Role |
|---|---|
| John Apollos | Group Leader |
| Kojo Lucas | Group A — EDA |
| Brenda Chepngeno | Group A — EDA |
| Tracey Mugo | Group B — Unsupervised |
| Linda Chepng'eno | Group B — Unsupervised |
| Lewis Njue | Group C — Supervised (Decision Tree, Logistic Regression) |
| Doreen Okenye | Group C — Supervised (Gradient Boosting, MLP) |
| Brian | Group C — Supervised (KNN, Naive Bayes) |
| Crispin Oigara | Group D — Evaluation & Documentation |
| Victor Kiptoo | Group D — Evaluation & Documentation |

## Course

**Unit:** Machine Learning 2  
**Institution:** JKUAT  
**Year:** 2026
