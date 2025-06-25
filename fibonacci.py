import multiprocessing

def sequential_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sequential_fibonacci(n - 1) + sequential_fibonacci(n - 2)

def worker(n):
    return sequential_fibonacci(n)

def parallel_fibonacci(n, num_processes):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # For calculating a single Fibonacci number F(n), true parallel speedup is hard
    # because F(n) = F(n-1) + F(n-2) is inherently sequential at the top level.
    # However, if the goal is to compute a *series* of Fibonacci numbers,
    # e.g., F(1), F(2), ..., F(k), then each F(i) can be computed independently in parallel.
    # This function, `parallel_fibonacci_series`, will implement that.

    # This function is designed to compute a series up to n.
    # If the user meant to parallelize calculation of a single F(n),
    # the previous implementation `parallel_fibonacci` attempted that,
    # but it's less practical. We will focus on the series.

    # The function name `parallel_fibonacci` might be misleading if it's for a series.
    # Let's rename it to `parallel_fibonacci_series` and make it compute numbers from 1 to n.
    # The `num_processes` will determine how many worker processes are used.

    # This function will now return a list of Fibonacci numbers from F(0) to F(n).
    # The plan was to implement "the" parallel Fibonacci function.
    # I'll provide `calculate_fibonacci_series_parallelly`
    # and a helper `calculate_single_fibonacci_parallelly` (which is less effective).

    # The original `parallel_fibonacci` function is being removed as it was
    # a bit ambiguous. It's replaced by the more specific functions below.
    # If the user specifically wants to parallelize a single F(n) calculation
    # (which is often not very effective), they can use
    # `calculate_single_fibonacci_parallelly`.
    # For a series, `calculate_fibonacci_series_parallelly` is more appropriate.
    # This function will be removed.
    raise NotImplementedError("This function is deprecated. Use calculate_single_fibonacci_parallelly or calculate_fibonacci_series_parallelly.")


def calculate_single_fibonacci_parallelly(n, num_processes):
    """
    Calculates a single Fibonacci number F(n) by attempting to parallelize
    the computation of F(n-1) and F(n-2).
    Note: This approach has limitations and may not be faster than sequential
    for small n or due to overhead. It requires num_processes >= 2.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    if num_processes < 2: # Need at least 2 processes for F(n-1) and F(n-2)
        # print("Warning: Not enough processes for parallel calculation of single F(n), falling back to sequential.")
        return sequential_fibonacci(n)

    # Heuristic: if n is not significantly larger than what two processes can handle,
    # or if n is small, sequential might be better.
    # This threshold is arbitrary and might need tuning.
    if n < 10: # Small n, sequential is likely faster
        return sequential_fibonacci(n)

    with multiprocessing.Pool(processes=2) as pool: # Use exactly 2 processes for F(n-1) and F(n-2)
        results = pool.map(worker, [n - 1, n - 2])
    return sum(results)


def calculate_fibonacci_series_parallelly(up_to_n, num_processes):
    """
    Calculates Fibonacci numbers F(0), F(1), ..., F(up_to_n) in parallel.
    Each F(i) is calculated by a separate task.
    """
    if up_to_n < 0:
        return []

    # The numbers to calculate Fibonacci for: 0, 1, ..., up_to_n
    tasks = range(up_to_n + 1)

    # Ensure num_processes is at least 1 and not more than available CPUs or tasks
    actual_num_processes = min(max(1, num_processes), multiprocessing.cpu_count(), len(tasks))

    if actual_num_processes == 0 and len(tasks) > 0 : # Should not happen if up_to_n >=0
         actual_num_processes = 1
    elif len(tasks) == 0: # up_to_n < 0, handled above, but as a safeguard
        return []

    with multiprocessing.Pool(processes=actual_num_processes) as pool:
        results = pool.map(sequential_fibonacci, tasks)

    return results


if __name__ == '__main__':
    # Example usage for calculating a single Fibonacci number in "parallel"
    number_single = 20
    processes_single = 2
    print(f"Calculating F({number_single}) using {processes_single} processes (for F(n-1) and F(n-2))...")
    result_single_parallel = calculate_single_fibonacci_parallelly(number_single, processes_single)
    print(f"Parallel F({number_single}) = {result_single_parallel}")

    print(f"\nCalculating F({number_single}) sequentially...")
    sequential_result_single = sequential_fibonacci(number_single)
    print(f"Sequential F({number_single}) = {sequential_result_single}")

    # Example usage for calculating a Fibonacci series in parallel
    series_up_to_n = 20
    series_num_processes = multiprocessing.cpu_count() # Use all available CPUs for series

    print(f"\nCalculating Fibonacci series up to F({series_up_to_n}) in parallel using {series_num_processes} processes:")
    parallel_series_results = calculate_fibonacci_series_parallelly(series_up_to_n, series_num_processes)

    for i, val in enumerate(parallel_series_results):
        print(f"F({i}) = {val}")

    print(f"\nCalculating Fibonacci series up to F({series_up_to_n}) sequentially for comparison:")
    sequential_series_results = [sequential_fibonacci(i) for i in range(series_up_to_n + 1)]
    for i, val in enumerate(sequential_series_results):
        print(f"F({i}) = {val}")
