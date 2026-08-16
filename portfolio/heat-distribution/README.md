# Heat Distribution Simulator

A compact 2-D Jacobi solver in C++17. Each iteration replaces a cell with the
average of its four neighbours. The OpenMP version parallelises the interior
update while keeping the boundary fixed, then checks convergence using the
maximum cell change.

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
./build/heat --size 256 --iterations 500 --threads 4
```

This project demonstrates stencil computation, data parallelism, convergence
criteria, and the importance of comparing parallel output with a sequential
reference.
