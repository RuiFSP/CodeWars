def flatten_and_sort(array: list) -> list:
    """
    Flatten and sort an array of integers in ascending order.

    :param array: list of integers
    :return: list of integers in ascending order
    """
    return sorted([item for sublist in array for item in sublist])


if __name__ == "__main__":
    assert flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten_and_sort([]) == []
    assert flatten_and_sort([[1, 3, 5], [-100], [2, 4, 6]]) == [-100, 1, 2, 3, 4, 5, 6]
    assert flatten_and_sort([[1, 1, 1], [2, 2, 2], [3, 3, 3]]) == [1, 1, 1, 2, 2, 2, 3, 3, 3]
    print("All tests passed successfully")