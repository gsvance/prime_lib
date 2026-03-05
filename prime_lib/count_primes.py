"""Count the number of primes less than some integer"""

from .prime_sieve import prime_sieve


def count_primes(n: int) -> int:
    """Return a count of how many primes are less than n."""
    if n <= 2:
        return 0  # No primes less than 2

    return sum(prime_sieve(n), start=0)
