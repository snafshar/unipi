# Heat Distribution Simulator

I implemented a compact 2-D Jacobi solver in C++17. At every iteration I
replace each interior cell with the average of its four neighbours. I kept the
boundary fixed and added an OpenMP-ready parallel update with a maximum-change
convergence check.

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
./build/heat --size 256 --iterations 500 --threads 4
```

I used this project to practise stencil computation, data parallelism, and
convergence criteria. Before reporting speedup, I compare the parallel result
with a sequential reference.
