# Seeds Dataset — ML2 Group Project

A machine learning analysis of the UCI Seeds dataset as part of our 
Machine Learning 2 coursework. The dataset contains 210 wheat kernel 
samples across three varieties (Kama, Rosa, and Canadian), described 
by seven geometric features extracted using soft X-ray imaging.

## Project Objectives

- Perform exploratory data analysis to understand feature distributions
  and class separability
- Apply unsupervised learning (K-Means, Hierarchical Clustering) and 
  compare recovered clusters against true labels using ARI and NMI
- Train and evaluate multiple supervised classifiers (KNN, Naive Bayes,
  Decision Tree, Logistic Regression, Random Forest, SVM, Gradient 
  Boosting, MLP)
- Tune hyperparameters using GridSearchCV and RandomizedSearchCV
- Compare top models using McNemar's statistical significance test

## Dataset

**Source:** UCI Machine Learning Repository  
**Citation:** Charytanowicz, M., Niewczas, J., Kulczycki, P., Kowalski, P., 
& Lukasik, S. (2010). Seeds [Dataset]. UCI Machine Learning Repository.  
https://doi.org/10.24432/C5H30K  
**License:** CC BY 4.0

| Property | Value |
|---|---|
| Instances | 210 |
| Features | 7 (all real-valued) |
| Classes | 3 (Kama, Rosa, Canadian) |
| Missing Values | None |
| Class Balance | Perfectly balanced (70 per class) |

## Repository Structure

```
seeds-ml2-analysis/
│
├── notebook/
│   ├── 00_starter_preprocessing.ipynb   # Shared base — all groups start here
│   ├── 01_eda.ipynb                     # Group A
│   ├── 02_unsupervised.ipynb            # Group B
│   ├── 03_supervised.ipynb              # Group C
│   └── 04_evaluation_report.ipynb       # Group D
│
├── report/
│   └── seeds_ml2_final_report.pdf
│
├── slides/
│   └── seeds_ml2_presentation.pptx
│
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone https://github.com/JohnApollos/ml2-seeds-analysis.git
cd seeds-ml2-analysis
pip install -r requirements.txt
```

## Requirements

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

## Team

| Member | Role |
|---|---|
| John Apollos | Group Leader |
| Kojo Lucas | Group A — EDA |
| Brenda Chepngeno | Group A — EDA |
| Tracey Mugo | Group B — Unsupervised |
| Linda Chepngeno | Group B — Unsupervised |
| Lewis Njue | Group C — Supervised (Decision Tree, Logistic Regression) |
| Doreen Okenye | Group C — Supervised (Gradient Boosting, MLP) |
| Brian | Group C — Supervised (KNN, Naive Bayes) |
| Crispin Oigara | Group D — Evaluation & Documentation |
| Victor Kiptoo | Group D — Evaluation & Documentation |

## Course

**Unit:** Machine Learning 2  
**Institution:** JKUAT  
**Year:** 2026
