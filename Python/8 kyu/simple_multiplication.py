def simple_multiplication(number: int) -> int:
    """
        Performs simple multiplication by eight if it is an even number and by nine otherwise.

    Args:
        number (int): The input number.

    Returns:
        int: The result of the multiplication.
    """

    return number * 8 if number % 2 == 0 else number * 9


if __name__ == "__main__":
    assert simple_multiplication(2) == 16
    assert simple_multiplication(1) == 9
    assert simple_multiplication(8) == 64
    assert simple_multiplication(4) == 32
    assert simple_multiplication(5) == 45
    print("All tests passed")