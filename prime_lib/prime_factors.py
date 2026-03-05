"""Reduce any integer to its set of prime factors."""

from typing import Literal, overload

from .prime_sieve import prime_sieve


@overload
def prime_factors(n: int, *, as_dict: Literal[False]) -> list[int]:
    ...


@overload
def prime_factors(n: int, *, as_dict: Literal[True]) -> dict[int, int]:
    ...


def prime_factors(n: int, *, as_dict: bool = False):
    """Reduce the integer n down to its prime factors and return a list.

    Alternatively, if as_dict is True, return the factors as a dict.
    """
    if n < 1:
        raise ValueError('can only reduce positive integers to prime factors')

    factors: dict[int, int] | list[int] = {} if as_dict else []
    if n == 1:
        return factors

    sieve = prime_sieve(n)

    for p, p_is_prime in enumerate(sieve):
        if p_is_prime:
            q, r = divmod(n, p)
            while r == 0:
                if as_dict:
                    factors[p] = factors.get(p, 0) + 1
                else:
                    factors.append(p)
                n = q
                q, r = divmod(n, p)
        if n == 1:
            break

    return factors
