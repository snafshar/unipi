# Parallel Word Count

A small, reproducible C++17 benchmark that compares a sequential word count
with a `std::thread` implementation. Input is split into line ranges, each
worker owns its local map, and the final reduction is deterministic and free of
shared-map contention.

## Build and run

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
./build/wordcount README.md --threads 4
```

The output reports the number of words, distinct words, elapsed time, and
speedup relative to the sequential baseline. A word is a maximal sequence of
ASCII letters or digits.

## Design notes

- No global lock protects the hot counting loop.
- Per-thread maps make ownership explicit.
- The reduction is sorted before printing, making results stable across runs.
- This is a teaching benchmark, not a claim that more threads always help;
  small files are dominated by startup and parsing overhead.
