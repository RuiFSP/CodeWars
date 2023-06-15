from typing import List


def prime_factors(n: int) -> List[int]:
    """
    Returns the prime factors of a given number.

    Args:
        n (int): The number to find prime factors for.

    Returns:
        List[int]: The list of prime factors of the given number.
    """
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor  # Use integer division instead of float division
        divisor += 1

    return factors


if __name__ == "__main__":
    assert prime_factors(1) == []
    assert prime_factors(2) == [2]
    assert prime_factors(3) == [3]
    assert prime_factors(4) == [2, 2]
    assert prime_factors(5) == [5]
    assert prime_factors(6) == [2, 3]
    assert prime_factors(7) == [7]
    assert prime_factors(8) == [2, 2, 2]
    assert prime_factors(9) == [3, 3]
    assert prime_factors(10) == [2, 5]
    assert prime_factors(11) == [11]
    assert prime_factors(12) == [2, 2, 3]
    print("All tests passed")
