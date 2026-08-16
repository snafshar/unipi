# PageRank

I implemented iterative PageRank with damping, dangling-node handling, and a
convergence tolerance. The code makes the update equation visible instead of
delegating it to a graph library.

```bash
python3 pagerank.py
```

My next experiment would compare convergence speed for sparse graphs with
different damping factors.
