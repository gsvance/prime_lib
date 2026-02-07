"""A function for finding a list of primes using the sieve of Eratosthenes."""


def prime_sieve(n: int) -> list[bool]:
    """Return a list of length n where element m is True when m is a prime."""
    if n < 0:
        raise ValueError("length of prime sieve cannot be negative")

    if n < 3:
        return [False, False][:n]

    sieve = [False, False] + [True] * (n - 2)

    number = 2
    while number ** 2 <= n:
        if sieve[number]:
            multiple = 2 * number
            while multiple < n:
                sieve[multiple] = False
                multiple += number
        number += 1

    return sieve
