# Map Reduce

I implemented a deterministic local MapReduce pipeline. I partition the input,
map each partition into a partial word count, and reduce the partial results
into one sorted output.

```bash
python3 map_reduce.py
```

This gives me a small correctness baseline before replacing the local executor
with MPI or a distributed runtime.
