#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

int main(int argc, char** argv) {
    int n = 128, iterations = 500, threads = 1;
    for (int i = 1; i + 1 < argc; i += 2) {
        std::string flag = argv[i];
        int* target = flag == "--size" ? &n : flag == "--iterations" ? &iterations : &threads;
        *target = std::stoi(argv[i + 1]);
    }
    if (n < 3 || iterations < 1 || threads < 1) return 2;
    std::vector<double> current(n * n, 0.0), next = current;
    for (int row = 0; row < n; ++row) current[row * n] = 100.0;
    double max_delta = 0.0;
    for (int step = 0; step < iterations; ++step) {
        max_delta = 0.0;
#ifdef _OPENMP
#pragma omp parallel for num_threads(threads) reduction(max:max_delta)
#endif
        for (int row = 1; row < n - 1; ++row) {
            for (int col = 1; col < n - 1; ++col) {
                const int index = row * n + col;
                next[index] = 0.25 * (current[index - 1] + current[index + 1]
                    + current[index - n] + current[index + n]);
                max_delta = std::max(max_delta, std::abs(next[index] - current[index]));
            }
        }
        std::swap(current, next);
        if (max_delta < 1e-5) { ++step; std::cout << "iterations=" << step; break; }
        if (step == iterations - 1) std::cout << "iterations=" << iterations;
    }
    double average = 0.0;
    for (double value : current) average += value;
    std::cout << " average=" << average / current.size() << " max_delta=" << max_delta << '\n';
}
