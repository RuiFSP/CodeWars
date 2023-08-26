def triangular(n: int) -> int:
    """
    Returns the nth triangular number.
    """
    return n * (n + 1) // 2 if n > 0 else 0


if __name__ == "__main__":
    sample_test_cases = [
        (0, 0),
        (2, 3),
        (3, 6),
        (4, 10),
        (9, 45),
        (-10, 0),
    ]

    for n, expected in sample_test_cases:
        assert triangular(n) == expected, f"triangular({n}) == {expected} failed"
