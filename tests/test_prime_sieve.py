"""Test that the prime_sieve is correctly generating lists of primes."""

import unittest

from prime_lib import prime_sieve


class TestPrimeSieve(unittest.TestCase):

    def test_prime_sieve_for_small_limits(self):
        self.assertListEqual(prime_sieve(4), [False, False, True, True])
        self.assertListEqual(
            prime_sieve(10),
            [
                False, False, True, True, False,
                True, False, True, False, False,
            ],
        )
        self.assertListEqual(
            prime_sieve(20),
            [
                False, False, True, True, False,
                True, False, True, False, False,
                False, True, False, True, False,
                False, False, True, False, True,
            ],
        )

    def test_prime_sieve_for_zero(self):
        self.assertListEqual(prime_sieve(0), [])

    def test_prime_sieve_using_indices(self):
        sieve = prime_sieve(10)
        self.assertListEqual([n for n in range(10) if sieve[n]], [2, 3, 5, 7])

    def test_prime_sieve_sum_one_hundred(self):
        self.assertEqual(sum(prime_sieve(100)), 25)
