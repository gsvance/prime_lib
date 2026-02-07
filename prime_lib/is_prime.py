"""A function for checking whether a single, isolated number is prime."""


def is_prime(n: int) -> bool:
    """Return whether n is a prime number."""
    if n < 2:
        return False

    divisor = 2
    while divisor ** 2 <= n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True
