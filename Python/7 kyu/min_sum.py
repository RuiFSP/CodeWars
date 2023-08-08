def min_sum(arr: list) -> int:
    """
    Given an array of integers of size N, our task is to write a program to find the minimum sum of the product of
    two elements of the array.
    :param arr: list of integers
    :return: minimum sum of the product of two elements of the array
    """

    arr.sort()
    return sum(arr[i] * arr[-i - 1] for i in range(len(arr) // 2))


if __name__ == "__main__":
    assert min_sum([5, 4, 2, 3]) == 22
    assert min_sum([12, 6, 10, 26, 3, 24]) == 342
    assert min_sum([9, 2, 8, 7, 5, 4, 0, 6]) == 74
    print("All tests passed successfully")
