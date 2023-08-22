def digits(n: int) -> int:
    """
    Returns the number of digits in a number
    """
    return len(str(n))


if __name__ == "__main__":
    assert digits(5) == 1
    assert digits(12345) == 5
    assert digits(9876543210) == 10
    print("All tests passed")
