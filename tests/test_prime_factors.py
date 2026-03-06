"""Tests to ensure the prime_factors functions works correctly."""

import unittest

from prime_lib import prime_factors


class TestPrimeFactors(unittest.TestCase):

    def test_prime_factors_as_list(self):
        self.assertListEqual(prime_factors(60), [2, 2, 3, 5])
        self.assertListEqual(prime_factors(60, as_dict=False), [2, 2, 3, 5])

    def test_prime_factors_as_dict(self):
        self.assertDictEqual(
            prime_factors(60, as_dict=True), {2: 2, 3: 1, 5: 1},
        )

    def test_prime_factors_for_small_numbers(self):
        self.assertListEqual(prime_factors(4), [2, 2])
        self.assertListEqual(prime_factors(3), [3])
        self.assertListEqual(prime_factors(2), [2])
        self.assertListEqual(prime_factors(1), [])
        with self.assertRaises(ValueError):
            prime_factors(0)
        with self.assertRaises(ValueError):
            prime_factors(-1)

        self.assertDictEqual(prime_factors(4, as_dict=True), {2: 2})
        self.assertDictEqual(prime_factors(3, as_dict=True), {3: 1})
        self.assertDictEqual(prime_factors(2, as_dict=True), {2: 1})
        self.assertDictEqual(prime_factors(1, as_dict=True), {})
        with self.assertRaises(ValueError):
            prime_factors(0, as_dict=True)
        with self.assertRaises(ValueError):
            prime_factors(-1, as_dict=True)

    def test_prime_factors_for_large_composite(self):
        composite = 2*2 * 3*3*3*3 * 11 * 13
        self.assertListEqual(
            prime_factors(composite), [2, 2, 3, 3, 3, 3, 11, 13],
        )
        self.assertDictEqual(
            prime_factors(composite, as_dict=True), {2: 2, 3: 4, 11: 1, 13: 1},
        )

    def test_prime_factors_for_large_prime(self):
        mersenne_prime = 524287
        self.assertListEqual(prime_factors(mersenne_prime), [mersenne_prime])
        self.assertDictEqual(
            prime_factors(mersenne_prime, as_dict=True), {mersenne_prime: 1},
        )
