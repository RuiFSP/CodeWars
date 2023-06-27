def square(n: int) -> int:
    """
    Returns the square of a number.

    :param n: The number to square.
    :return: The square of the number.
    """
    return n * n


def test_square() -> None:
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(5) == 25


if __name__ == '__main__':
    test_square()
    print('All tests passed.')
