def find_average(nums:  list) -> float:
    """
    Find the average of a list of numbers.
    :param nums: list of numbers
    :return: average of the list of numbers.
    """
    if not nums:
        return 0
    return sum(nums) / len(nums)


if __name__ == "__main__":
    assert find_average([1, 1, 1]) == 1
    assert find_average([1, 2, 3]) == 2
    assert find_average([1, 2, 3, 4]) == 2.5
    assert find_average([1, 2, 3, 4, 5]) == 3
    assert find_average([1, 2, 3, 4, 5, 6]) == 3.5
    assert find_average([1, 2, 3, 4, 5, 6, 7]) == 4
    assert find_average([]) == 0
    assert find_average([-1, 3, 5, -7]) == 0
    print("All tests passed!")
