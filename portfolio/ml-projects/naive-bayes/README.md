# Naive Bayes

I implemented a multinomial Naive Bayes text classifier using token counts,
class priors, and Laplace smoothing. I use log probabilities to avoid numeric
underflow during classification.

```bash
python3 naive_bayes.py
```

I would add token normalisation, a held-out evaluation set, and a confusion
matrix in the next sprint.
