def get_real_floor(n: int) -> int:
    """
    Return the real floor of a given floor number.
    """
    if n <= 0:
        return n
    elif n <= 13:
        return n - 1
    else:
        return n - 2


if __name__ == "__main__":
    assert get_real_floor(1) == 0
    assert get_real_floor(5) == 4
    assert get_real_floor(15) == 13
    print("All tests passed")