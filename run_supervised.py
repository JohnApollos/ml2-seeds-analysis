import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Ensure directories exist
os.makedirs('plots/supervised', exist_ok=True)
os.makedirs('results/supervised', exist_ok=True)
os.makedirs('data', exist_ok=True)

# 1. Preprocessing (Phase 1 single source of truth)
cols = ["area", "perimeter", "compactness", "kernel_length", "kernel_width", "asymmetry_coefficient", "kernel_groove_length", "label"]
df = pd.read_csv("data/seeds_dataset.tsv", sep=r"\s+", header=None, names=cols)

X = df.drop(columns=['label'])
y = df['label']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)
X_scaled_df['label'] = y.values

X_scaled_df.to_csv('data/seeds_preprocessed.csv', index=False)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# Helper function to evaluate and save
def evaluate_models(models, filename):
    results = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results.append({
            'Model': name,
            'Accuracy': accuracy_score(y_test, y_pred),
            'Precision': precision_score(y_test, y_pred, average='macro'),
            'Recall': recall_score(y_test, y_pred, average='macro'),
            'F1-Score': f1_score(y_test, y_pred, average='macro')
        })
    results_df = pd.DataFrame(results)
    results_df.to_csv(f'results/supervised/{filename}', index=False)
    return results_df

# Person 1 (Brian) - KNN, Naive Bayes
models_p1 = {
    'KNN': GridSearchCV(KNeighborsClassifier(), {'n_neighbors': [3, 5, 7, 9]}),
    'Naive Bayes': GaussianNB()
}
evaluate_models(models_p1, 'brian_results.csv')

# Person 2 (Lewis) - Decision Tree, Logistic Regression
models_p2 = {
    'Decision Tree': GridSearchCV(DecisionTreeClassifier(random_state=42), {'max_depth': [3, 5, 7, None]}),
    'Logistic Regression': GridSearchCV(LogisticRegression(random_state=42), {'C': [0.1, 1, 10]})
}
evaluate_models(models_p2, 'lewis_results.csv')

# Person 3 (Unassigned) - Random Forest, SVM
rf = RandomForestClassifier(random_state=42)
models_p3 = {
    'Random Forest': GridSearchCV(rf, {'n_estimators': [50, 100], 'max_depth': [3, 5, None]}),
    'SVM': GridSearchCV(SVC(random_state=42), {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']})
}
evaluate_models(models_p3, 'apollos_results.csv')

# Feature Importance Plot (Random Forest)
best_rf = models_p3['Random Forest'].best_estimator_
importances = best_rf.feature_importances_
plt.figure(figsize=(10, 6))
sns.barplot(x=importances, y=X.columns)
plt.title('Feature Importances (Random Forest)')
plt.tight_layout()
plt.savefig('plots/supervised/feature_importance.png')

# Person 4 (Doreen) - Gradient Boosting, MLP
models_p4 = {
    'Gradient Boosting': GridSearchCV(GradientBoostingClassifier(random_state=42), {'n_estimators': [50, 100], 'learning_rate': [0.01, 0.1]}),
    'MLP': GridSearchCV(MLPClassifier(max_iter=1000, random_state=42), {'hidden_layer_sizes': [(50,), (100,)]})
}
evaluate_models(models_p4, 'doreen_results.csv')

print("Supervised learning complete!")
