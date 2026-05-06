# Unsupervised Learning Notebook - Execution Guide

## Quick Start

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy
```

### Step 1: Navigate to notebook directory
```bash
cd notebook
```

### Step 2: Launch Jupyter
```bash
jupyter notebook 02_unsupervised.ipynb
```

### Step 3: Run all cells
- Use "Cell → Run All" or press Ctrl+Alt+Enter
- Cells are ordered for sequential execution
- All dependencies are imported at the start

## Cell-by-Cell Breakdown

### Section 1: Load and Prepare Data (Cells 1-4)
- Import libraries
- Load dataset from data/seeds_dataset.tsv
- Verify structure and distribution
- Apply StandardScaler preprocessing
- **Expected**: Shape (210, 7), standardized features with mean≈0, std≈1

### Section 2: Elbow Method (Cells 5-7)
- Run K-Means for k=2 to k=8
- Plot inertia vs k
- **Expected**: Clear elbow at k=3, plot saved to plots/elbow_curve.png

### Section 3: Final K-Means (Cell 8)
- Fit K-Means with k=3, random_state=42
- Print cluster distribution
- **Expected**: 3 clusters with roughly 70 samples each

### Section 4: PCA Visualization (Cells 9-10)
- Apply PCA to 2D
- Create side-by-side scatter plots
- **Expected**: Two visualizations showing K-Means vs True labels
- **Output**: plots/kmeans_vs_true_pca.png

### Section 5: Cluster Centers (Cells 11-12)
- Print centers in standardized space
- Print centers in original feature space
- Create heatmap visualization
- **Expected**: 3 rows (clusters) × 7 columns (features)
- **Output**: plots/cluster_centers_heatmap.png

### Section 6: K-Means Evaluation (Cell 13)
- Compute Adjusted Rand Index
- Compute Normalized Mutual Information
- Print evaluation metrics
- **Expected**: ARI and NMI scores reported

### Section 7: Interpretation (Cell 14)
- Generate detailed interpretation paragraph
- Save to results/kmeans_evaluation.txt
- **Expected**: ~200 word interpretation of metric meaning

### Section 8: Hierarchical Clustering (Cell 15)
- Fit Agglomerative Clustering
- Compute ARI and NMI
- Print distribution and metrics
- **Expected**: 3 clusters with ARI/NMI scores

### Section 9: Dendrogram (Cell 16)
- Compute linkage matrix
- Plot dendrogram with cut line for k=3
- **Expected**: Tree visualization with truncation
- **Output**: plots/dendrogram.png

### Section 10: Comparison Visualization (Cell 17)
- Three-way PCA comparison plot
- Hierarchical, K-Means, True labels
- **Expected**: 3-panel figure
- **Output**: plots/clustering_comparison_pca.png

### Section 11: Comparison Table (Cells 18-19)
- Print text comparison table
- Create visual comparison table
- **Expected**: Table with metrics and visual styling
- **Output**: plots/clustering_comparison_table.png

### Section 12: Final Summary (Cell 20)
- Generate comprehensive summary report
- Save to results/unsupervised_analysis_summary.txt
- **Expected**: ~50-line detailed report

### Section 13: Methodological Notes (Cell 21)
- Reference information and limitations
- Documentation of preprocessing and algorithms
- **Expected**: Informational markdown, no computation

## Expected Runtime
- Total execution time: ~2-3 minutes
- Slowest steps:
  - Elbow method with 7 K-Means runs: ~30 seconds
  - Dendrogram linkage computation: ~15 seconds
  - PCA visualization: ~10 seconds

## Output Directory Structure
```
project_root/
├── notebook/
│   └── 02_unsupervised.ipynb (THIS FILE)
├── plots/
│   ├── elbow_curve.png
│   ├── kmeans_vs_true_pca.png
│   ├── cluster_centers_heatmap.png
│   ├── dendrogram.png
│   ├── clustering_comparison_pca.png
│   └── clustering_comparison_table.png
├── results/
│   ├── kmeans_evaluation.txt
│   ├── unsupervised_analysis_summary.txt
│   └── unsupervised_deliverable_summary.md
└── data/
    └── seeds_dataset.tsv
```

## Troubleshooting

### Issue: Data file not found
**Solution**: Ensure you're running from the notebook directory, or adjust the path to `../data/seeds_dataset.tsv`

### Issue: ImportError for numpy/scipy/etc
**Solution**: Install missing package with `pip install <package_name>`

### Issue: Plots directory doesn't exist
**Solution**: The notebook creates it automatically, but manually create `plots/` and `results/` directories if needed

### Issue: Kernel crashes on dendrogram
**Solution**: This can happen with very large datasets. The notebook uses truncation (p=30) to prevent this

### Issue: Memory error
**Solution**: The dataset is only 210 samples, shouldn't cause memory issues. Check system resources or restart kernel.

## Customization

### Change k value
- Modify line in Elbow Method section: `k_values = range(2, 9)`
- Modify final K-Means: `kmeans_final = KMeans(n_clusters=3, ...)`

### Change linkage method for hierarchical clustering
- Modify: `hierarchical_clusterer = AgglomerativeClustering(n_clusters=3, linkage='ward')`
- Options: 'ward', 'complete', 'average', 'single'

### Change random state
- Modify: `random_state=42` throughout notebook
- Use different integer for different randomization

### Change color scheme
- Modify: `colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']`
- Use any valid matplotlib colors

## Interpreting Results

### Understanding ARI/NMI Scores
- **ARI > 0.5**: Good agreement with true labels
- **ARI 0-0.5**: Moderate agreement
- **ARI < 0**: Worse than random labeling

- **NMI > 0.7**: Strong agreement
- **NMI 0.4-0.7**: Moderate agreement
- **NMI < 0.4**: Weak agreement

### Comparing Methods
- Higher ARI/NMI = Better recovery of true structure
- Visual inspection of PCA plots also important
- Consider trade-offs: speed vs interpretability

## Integration with Supervised Learning

Results from this analysis can inform:
1. Feature importance (from cluster interpretation)
2. Label balancing confirmation (3 balanced classes)
3. Natural grouping assessment (for semi-supervised methods)
4. Baseline clustering quality (for comparison with supervised approaches)

---

**Document Version**: 1.0  
**Last Updated**: May 2026  
**Status**: Ready for execution
