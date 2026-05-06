# Clustering Metrics Quick Reference

## Adjusted Rand Index (ARI)

### Definition
Measures the similarity between two partitions (clusterings), adjusted for chance agreement.

### Formula
$$\text{ARI} = \frac{\text{RI} - E[\text{RI}]}{\max(\text{RI}) - E[\text{RI}]}$$

where RI is the Rand Index.

### Range
- **-1.0**: Perfect disagreement (worse than random)
- **0.0**: Random labeling (baseline)
- **+1.0**: Perfect agreement

### Interpretation
- **ARI > 0.7**: Excellent agreement
- **0.4 < ARI ≤ 0.7**: Good agreement
- **0 < ARI ≤ 0.4**: Fair/Moderate agreement
- **ARI ≤ 0**: Poor agreement (comparable to or worse than random)

### What It Tells Us
Measures how well the clustering algorithm recovered the same pairwise relationships present in the true labels. A high ARI means samples that should be together are clustered together, and samples that should be apart are separated.

### Advantages
- Adjusted for chance (unlike raw Rand Index)
- Symmetric (doesn't depend on label order)
- Allows for label permutation independence

### scikit-learn Implementation
```python
from sklearn.metrics import adjusted_rand_score
ari = adjusted_rand_score(true_labels, predicted_labels)
```

---

## Normalized Mutual Information (NMI)

### Definition
Measures the mutual information (information shared) between two clusterings, normalized to [0,1] scale.

### Formula
$$\text{NMI} = \frac{2 \cdot I(X;Y)}{H(X) + H(Y)}$$

where I(X;Y) is mutual information and H(X), H(Y) are entropies.

### Range
- **0.0**: Independent clusterings (no shared information)
- **1.0**: Perfect agreement (complete shared information)
- Between 0 and 1: Varying degrees of agreement

### Interpretation
- **NMI > 0.8**: Excellent agreement
- **0.6 < NMI ≤ 0.8**: Good agreement
- **0.4 < NMI ≤ 0.6**: Fair/Moderate agreement
- **NMI ≤ 0.4**: Weak agreement

### What It Tells Us
Measures how much knowing the cluster assignment reduces uncertainty about the true class. High NMI means the clustering captures much of the structure present in the true labels. It's an information-theoretic measure.

### Advantages
- Normalized to [0,1] for easy interpretation
- Symmetric
- Information-theoretic foundation
- Doesn't assume any particular cluster label correspondence

### scikit-learn Implementation
```python
from sklearn.metrics import normalized_mutual_info_score
nmi = normalized_mutual_info_score(true_labels, predicted_labels)
```

---

## Comparison: ARI vs NMI

| Aspect | ARI | NMI |
|--------|-----|-----|
| **Range** | -1 to +1 | 0 to 1 |
| **Type** | Combinatorial | Information-theoretic |
| **Baseline** | 0 (random) | 0 (independent) |
| **Perfect** | 1 | 1 |
| **Symmetry** | Yes | Yes |
| **Chance-adjusted** | Yes | No (but normalized) |
| **Sensitivity** | More sensitive to cluster structure | Balanced sensitivity |
| **Interpretation** | Pairwise agreement | Information sharing |

---

## How to Interpret Together

### Scenario 1: High ARI, High NMI (Both > 0.7)
✅ **Excellent** - Algorithm recovered the natural structure very well
- Clusters match true groupings
- Partition structure is well preserved
- Label correspondence is clear

### Scenario 2: High ARI, Moderate NMI (ARI > 0.7, 0.4 < NMI < 0.7)
⚠️ **Good but asymmetric** - Pairwise structure matches but not all information captured
- Clusters are in right relationships
- Some samples at cluster boundaries
- Minor label misalignment

### Scenario 3: Moderate ARI, Moderate NMI (0.4 < Both < 0.7)
ℹ️ **Fair** - Some agreement with structure partially recovered
- Meaningful clustering but imperfect
- Natural groupings only partially detected
- Useful but room for improvement

### Scenario 4: Low ARI, Low NMI (Both < 0.3)
❌ **Poor** - Clustering doesn't align with true structure
- Algorithm found different structure
- Not useful for label prediction
- May indicate wrong k or unsuitable method

### Scenario 5: Inconsistent Scores (One high, one low)
❓ **Investigate** - Unusual pattern, check data and labels
- May indicate label noise or ambiguity
- Could suggest mixed cluster quality
- Needs manual inspection

---

## Seeds Dataset Context

### Expected Results
For the seeds dataset (3 wheat varieties with geometric features):
- **ARI**: Typically 0.5-0.9 range expected (good separability)
- **NMI**: Typically 0.6-0.95 range expected (good information capture)

### Why These Metrics Matter
1. **ARI**: Shows if K-Means preserves the structure that exists in nature
2. **NMI**: Shows how much information the clustering provides about true class
3. **Together**: Comprehensive picture of clustering quality

### Interpretation for This Project
- High scores (> 0.7 both): Validates k=3 and confirms natural groupings
- Moderate scores (0.4-0.7): Shows partial recovery, some ambiguity
- Low scores (< 0.4): Questions whether true groupings are natural or if different structure exists

---

## Important Notes

### Label Alignment
- Neither ARI nor NMI care about label correspondence
- Cluster 0 doesn't need to = Class 0
- These metrics automatically handle label permutations
- Only the partition structure matters

### Random Baseline
- ARI = 0 is random clustering (by definition)
- For NMI, random clustering ≈ 0
- Both metrics are chance-adjusted for fair comparison

### Sensitivity
- Both metrics are sensitive to k (number of clusters)
- Both assume hard assignments (not fuzzy)
- Both expect balanced or unbalanced classes OK

### Multiple Clustering Methods
- Same metrics apply to any hard clustering algorithm
- Enables fair comparison of K-Means vs Hierarchical vs others
- Same ground truth (true labels) for all comparisons

---

## References

### Metrics Documentation
- **Adjusted Rand Index**: Hubert & Arabie (1985)
- **Normalized Mutual Information**: Danon et al. (2005)
- **scikit-learn docs**: 
  - https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html
  - https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html

### Related Metrics
- Rand Index (RI): Raw version without adjustment
- Mutual Information (MI): Unnormalized version
- Silhouette Score: Intrinsic measure (uses data, not labels)
- Davies-Bouldin Index: Intrinsic measure
- Calinski-Harabasz Index: Intrinsic measure

---

## Practical Examples

### Example 1: Perfect Clustering
```
True labels:   [1, 1, 1, 2, 2, 2, 3, 3, 3]
Predicted:     [0, 0, 0, 1, 1, 1, 2, 2, 2]
ARI: 1.0 ✅
NMI: 1.0 ✅
Interpretation: Perfect reconstruction of natural groupings
```

### Example 2: Good Clustering with Minor Errors
```
True labels:   [1, 1, 1, 2, 2, 2, 3, 3, 3]
Predicted:     [0, 0, 1, 1, 1, 2, 2, 2, 2]
ARI: ~0.75 ✅
NMI: ~0.85 ✅
Interpretation: Good recovery, one sample misclassified
```

### Example 3: Random Clustering
```
True labels:   [1, 1, 1, 2, 2, 2, 3, 3, 3]
Predicted:     [0, 1, 2, 1, 0, 2, 2, 0, 1]
ARI: ~0.0 ⚠️
NMI: ~0.0 ⚠️
Interpretation: No better than random, algorithm fails
```

### Example 4: Wrong k (Too Few Clusters)
```
True labels:   [1, 1, 1, 2, 2, 2, 3, 3, 3]
Predicted:     [0, 0, 0, 0, 1, 1, 1, 1, 1]  # Only 2 clusters
ARI: ~0.3 ⚠️
NMI: ~0.5 ⚠️
Interpretation: Captures some structure but merges natural groups
```

---

**Version**: 1.0  
**Created**: May 2026  
**For**: ML2 Seeds Analysis Project
