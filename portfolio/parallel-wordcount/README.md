# Parallel Word Count

I built this C++17 benchmark to compare sequential word counting with a
`std::thread` implementation. I split the input into line ranges, give each
worker a local map, and perform a deterministic final reduction without shared
hot-path contention.

## Build and run

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
./build/wordcount README.md --threads 4
```

The output reports total words, distinct words, elapsed time, and speedup
relative to my sequential baseline. I define a word as a maximal sequence of
ASCII letters or digits.

## Design notes

- No global lock protects the hot counting loop.
- Per-thread maps make ownership explicit.
- The reduction is sorted before printing, making results stable across runs.
- This is a teaching benchmark, not a claim that more threads always help;
  small files are dominated by startup and parsing overhead.
