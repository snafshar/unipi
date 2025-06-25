import unittest
import multiprocessing
from fibonacci import sequential_fibonacci, calculate_single_fibonacci_parallelly, calculate_fibonacci_series_parallelly

class TestFibonacci(unittest.TestCase):

    def test_sequential_fibonacci(self):
        self.assertEqual(sequential_fibonacci(0), 0)
        self.assertEqual(sequential_fibonacci(1), 1)
        self.assertEqual(sequential_fibonacci(2), 1)
        self.assertEqual(sequential_fibonacci(3), 2)
        self.assertEqual(sequential_fibonacci(10), 55)
        self.assertEqual(sequential_fibonacci(20), 6765)

    def test_calculate_single_fibonacci_parallelly(self):
        # Test with small n, fallback to sequential might occur or parallel is trivial
        self.assertEqual(calculate_single_fibonacci_parallelly(0, 2), 0)
        self.assertEqual(calculate_single_fibonacci_parallelly(1, 2), 1)
        self.assertEqual(calculate_single_fibonacci_parallelly(2, 2), 1) # n < 10, so sequential
        self.assertEqual(calculate_single_fibonacci_parallelly(3, 2), 2) # n < 10, so sequential

        # Test with n large enough for parallel attempt
        # Note: True parallelism for single F(n) is limited.
        # For n=10, sequential is 55. Parallel should match.
        self.assertEqual(calculate_single_fibonacci_parallelly(10, 2), 55)
        self.assertEqual(calculate_single_fibonacci_parallelly(15, 2), sequential_fibonacci(15))
        self.assertEqual(calculate_single_fibonacci_parallelly(20, 2), sequential_fibonacci(20))

        # Test with insufficient processes (should fallback to sequential)
        self.assertEqual(calculate_single_fibonacci_parallelly(10, 1), sequential_fibonacci(10))
        self.assertEqual(calculate_single_fibonacci_parallelly(15, 1), sequential_fibonacci(15))

    def test_calculate_fibonacci_series_parallelly(self):
        # Test empty series
        self.assertEqual(calculate_fibonacci_series_parallelly(-1, 2), [])

        # Test series up to 0
        self.assertEqual(calculate_fibonacci_series_parallelly(0, 2), [0])

        # Test series up to 1
        self.assertEqual(calculate_fibonacci_series_parallelly(1, 2), [0, 1])

        # Test series up to 10
        expected_series_10 = [sequential_fibonacci(i) for i in range(11)]
        self.assertEqual(calculate_fibonacci_series_parallelly(10, 2), expected_series_10)
        self.assertEqual(calculate_fibonacci_series_parallelly(10, 4), expected_series_10) # More processes

        # Test with more items than CPU cores to ensure pooling works
        # (assuming at least 1 CPU core for the test environment)
        num_cpus = multiprocessing.cpu_count()
        series_len = 15
        expected_series_15 = [sequential_fibonacci(i) for i in range(series_len + 1)]

        # Test with num_processes = 1
        self.assertEqual(calculate_fibonacci_series_parallelly(series_len, 1), expected_series_15)

        # Test with num_processes = num_cpus
        self.assertEqual(calculate_fibonacci_series_parallelly(series_len, num_cpus), expected_series_15)

        # Test with num_processes > num_cpus (should cap at num_cpus or len(tasks))
        self.assertEqual(calculate_fibonacci_series_parallelly(series_len, num_cpus * 2), expected_series_15)

        # Test with num_processes > len(tasks)
        small_series_len = 3
        expected_small_series = [sequential_fibonacci(i) for i in range(small_series_len + 1)]
        self.assertEqual(calculate_fibonacci_series_parallelly(small_series_len, num_cpus), expected_small_series)


if __name__ == '__main__':
    unittest.main()
