def max_multiple(divisor: int, bound: int) -> int:
    """
    Given a divisor and a bound, find the largest integer N such that:
    N is divisible by divisor.
    N is less than or equal to bound.
    N is greater than 0.
    """
    return bound - (bound % divisor)


if __name__ == "__main__":
    assert max_multiple(3, 10) == 9
    assert max_multiple(2, 7) == 6
    assert max_multiple(7, 17) == 14
    assert max_multiple(10, 50) == 50
    assert max_multiple(37, 200) == 185
    assert max_multiple(7, 100) == 98
    print("All tests passed")
