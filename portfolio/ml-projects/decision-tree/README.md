# Decision Tree

I implemented a small, interpretable decision stump. It evaluates candidate
features and thresholds and selects the split with the lowest weighted Gini
impurity.

```bash
python3 decision_tree.py
```

I would extend it with recursive tree growth, pruning, and train/test metrics.
