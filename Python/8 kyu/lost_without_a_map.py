def maps(a: list) -> list:
    """
    Given an array of integers, return a new array with each value doubled.
    :param a: list of integers
    :return: list of integers
    """
    return [x * 2 for x in a]


if __name__ == "__main__":
    assert maps([1, 2, 3]) == [2, 4, 6]
    assert maps([4, 1, 1, 1, 4]) == [8, 2, 2, 2, 8]
    assert maps([2, 2, 2, 2, 2, 2]) == [4, 4, 4, 4, 4, 4]
    print("All tests passed")