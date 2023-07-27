def no_boring_zeros(n: int) -> int:
    """
    Return the integer after removing any trailing zeros.
    """
    return int(str(n).rstrip('0')) if n else 0


if __name__ == "__main__":
    assert no_boring_zeros(1450) == 145
    assert no_boring_zeros(960000) == 96
    assert no_boring_zeros(1050) == 105
    assert no_boring_zeros(-1050) == -105
    assert no_boring_zeros(0) == 0
    assert no_boring_zeros(1) == 1
    print("All tests passed successfully!")