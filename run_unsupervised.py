import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score
from scipy.cluster.hierarchy import dendrogram, linkage

os.makedirs('plots/unsupervised', exist_ok=True)

df = pd.read_csv("data/seeds_preprocessed.csv")
X_scaled = df.drop(columns=['label']).values
y = df['label'].values

# K-Means Elbow Curve
inertias = []
for k in range(2, 9):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.figure()
plt.plot(range(2, 9), inertias, marker='o')
plt.title('Elbow Curve for K-Means')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.savefig('plots/unsupervised/elbow_curve.png')

# K-Means with k=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)

# PCA Plot
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure()
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans_labels, cmap='viridis')
plt.title('PCA Plot of K-Means Clusters')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(scatter, label='Cluster')
plt.savefig('plots/unsupervised/pca_kmeans.png')

# Hierarchical Clustering & Dendrogram
linked = linkage(X_scaled, 'ward')
plt.figure(figsize=(10, 7))
dendrogram(linked, truncate_mode='lastp', p=30)
plt.title('Hierarchical Clustering Dendrogram')
plt.savefig('plots/unsupervised/dendrogram.png')

agg_cluster = AgglomerativeClustering(n_clusters=3)
agg_labels = agg_cluster.fit_predict(X_scaled)

# ARI and NMI
results = [
    {
        'Algorithm': 'K-Means',
        'ARI': adjusted_rand_score(y, kmeans_labels),
        'NMI': normalized_mutual_info_score(y, kmeans_labels)
    },
    {
        'Algorithm': 'Hierarchical Clustering',
        'ARI': adjusted_rand_score(y, agg_labels),
        'NMI': normalized_mutual_info_score(y, agg_labels)
    }
]

pd.DataFrame(results).to_csv('results/unsupervised_results.csv', index=False)

print("Unsupervised learning complete!")
