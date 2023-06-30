from typing import List, Tuple


def decomp(n: int) -> str:
    """
    Decomposes n! (factorial n) into its prime factors.

    Args:
        n (int): The number for which factorial decomposition is required.

    Returns:
        str: The prime factor decomposition of n!.
    """
    primes = [True] * (n + 1)
    factors = []  # type: List[Tuple[int, int]]

    for p in range(2, n + 1):
        if primes[p]:
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            factors.append((p, count))

            for i in range(p, n + 1, p):
                primes[i] = False

    result = ''
    for factor in factors:
        if factor[1] == 1:
            result += str(factor[0]) + ' * '
        else:
            result += str(factor[0]) + '^' + str(factor[1]) + ' * '

    return result[:-3]  # Remove the last ' * '


if __name__ == "__main__":
    assert decomp(5) == "2^3 * 3 * 5"
    assert decomp(14) == "2^11 * 3^5 * 5^2 * 7^2 * 11 * 13"
    assert decomp(17) == "2^15 * 3^6 * 5^3 * 7^2 * 11 * 13 * 17"
    assert decomp(22) == "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"
    print("All tests passed successfully!")
