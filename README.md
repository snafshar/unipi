# unipi

## Parallel Fibonacci Calculator

This project provides Python implementations for calculating Fibonacci numbers, including:
- A standard sequential recursive Fibonacci function.
- A function to calculate a single Fibonacci number F(n) by attempting to parallelize the computation of F(n-1) and F(n-2). This method has limited speedup potential due to the overhead of multiprocessing and the inherent nature of the Fibonacci sequence.
- A function to calculate a series of Fibonacci numbers (F(0) to F(n)) in parallel, where each number in the series is computed as an independent task. This is generally a more effective use of parallelism for Fibonacci calculations.

### Files
- `fibonacci.py`: Contains the core logic for sequential and parallel Fibonacci calculations.
- `test_fibonacci.py`: Contains unit tests for the Fibonacci functions.

### How to Run

1.  **Run the Fibonacci script directly:**
    The `fibonacci.py` script includes an example `if __name__ == '__main__':` block that demonstrates the usage of the functions and prints results to the console.
    ```bash
    python fibonacci.py
    ```

2.  **Run the unit tests:**
    To verify the correctness of the implementations:
    ```bash
    python -m unittest test_fibonacci.py
    ```

### Parallelism Approach

-   **`calculate_single_fibonacci_parallelly(n, num_processes)`**:
    -   Attempts to speed up the calculation of a single F(n) by launching two processes for F(n-1) and F(n-2).
    -   Requires `num_processes >= 2`.
    -   May fall back to sequential calculation for small `n` or if `num_processes < 2`, as parallel overhead would dominate.
    -   Due to Python's Global Interpreter Lock (GIL) and the overhead of process creation, this method might not show significant speedup for CPU-bound tasks like this recursive Fibonacci implementation unless `n` is very large and the subproblems are substantial.

-   **`calculate_fibonacci_series_parallelly(up_to_n, num_processes)`**:
    -   Calculates all Fibonacci numbers from F(0) up to F(`up_to_n`).
    -   Each F(i) is treated as an independent task and distributed among a pool of worker processes.
    -   `num_processes` determines the size of the worker pool, typically set to `multiprocessing.cpu_count()` for optimal performance on CPU-bound tasks.
    -   This approach is generally more effective for leveraging multiple cores, as the tasks (calculating individual Fibonacci numbers) are independent and can be truly run in parallel.

### Benefits of Parallel Calculation (for Series)

-   **Speedup for Series**: When calculating a large series of Fibonacci numbers, distributing the work across multiple CPU cores can significantly reduce the total computation time compared to a purely sequential approach.
-   **Resource Utilization**: Makes better use of multi-core processors by keeping multiple cores busy.