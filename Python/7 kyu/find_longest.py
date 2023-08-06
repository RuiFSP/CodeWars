def find_longest(arr: list) -> int:
    """
    Find longest number in list of numbers.
    :param arr: list of numbers
    :return: longest number in list of numbers.
    """
    return max(arr, key=lambda x: len(str(x)))


if __name__ == "__main__":
    assert find_longest([1, 10, 100]) == 100
    assert find_longest([9000, 8, 800]) == 9000
    assert find_longest([8, 900, 500]) == 900
    assert find_longest([3, 300, 200]) == 300
    assert find_longest([3, 30, 20]) == 30
    print("All tests passed successfully")