"""A small library of integer functions related to prime numbers."""

from .count_primes import count_primes
from .is_prime import is_prime
from .prime_sieve import prime_sieve


__all__ = [
    "count_primes",
    "is_prime",
    "prime_sieve",
]
