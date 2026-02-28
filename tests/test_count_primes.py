"""Test that the count_primes function works as expected."""

import unittest

from prime_lib import count_primes


class TestPrimeSieve(unittest.TestCase):

    def test_count_primes_for_small_values(self):
        self.assertEqual(count_primes(2), 0)
        self.assertEqual(count_primes(3), 1)
        self.assertEqual(count_primes(4), 2)
        self.assertEqual(count_primes(5), 2)
        self.assertEqual(count_primes(6), 3)
        self.assertEqual(count_primes(7), 3)
        self.assertEqual(count_primes(8), 4)
        self.assertEqual(count_primes(9), 4)
        self.assertEqual(count_primes(10), 4)

    def test_count_primes_for_larger_values(self):
        self.assertEqual(count_primes(100), 25)
        self.assertEqual(count_primes(1_000), 168)

    def test_count_primes_below_two(self):
        for i in range(1, 11):
            self.assertEqual(count_primes(2 - i), 0)
