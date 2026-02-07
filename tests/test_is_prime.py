"""Test that is_prime can distinguish primes from non-prime numbers."""

import unittest

from prime_lib import is_prime


class TestIsPrime(unittest.TestCase):

    def test_is_prime_on_small_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))

    def test_is_prime_on_small_composites(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(16))
        self.assertFalse(is_prime(18))
        self.assertFalse(is_prime(20))

    def test_is_prime_on_numbers_below_two(self):
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-4))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
