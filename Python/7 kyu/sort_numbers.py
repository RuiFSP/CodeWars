def solution(nums: list) -> list:
    """
    Sort the numbers in ascending order.

    :param nums: list of numbers
    :return: sorted list of numbers or empty list if nums is None or empty.
    """
    return sorted(nums) if nums else []


if __name__ == "__main__":
    assert solution([1, 2, 3, 10, 5]) == [1, 2, 3, 5, 10]
    assert solution(None) == []
    assert solution([]) == []
    assert solution([20, 2, 10]) == [2, 10, 20]
    assert solution([2, 20, 10]) == [2, 10, 20]
    print("Coding complete? Click 'Check' to earn cool rewards!")
