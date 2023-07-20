def is_even(n: int) -> bool:
    """
    Returns True if n is even, False otherwise.
    """
    return n % 2 == 0


if __name__ == "__main__":
    assert is_even(0) == True
    assert is_even(0.5) == False
    assert is_even(1) == False
    assert is_even(2) == True
    assert is_even(-4) == True
    assert is_even(15) == False
    print("All tests passed successfully.")