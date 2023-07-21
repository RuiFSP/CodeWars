from typing import List

def divisible_by(numbers: List[int], divisor: int) -> List[int]:
    """
    Returns a list of numbers from the input list that are divisible by the given divisor.

    Parameters:
        numbers (List[int]): The list of numbers to filter.
        divisor (int): The divisor to check divisibility against.

    Returns:
        List[int]: A list of numbers that are divisible by the given divisor.
    """
    return [number for number in numbers if number % divisor == 0]


if __name__ == "__main__":
    assert divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
    assert divisible_by([1, 2, 3, 4, 5, 6], 3) == [3, 6]
    assert divisible_by([0, 1, 2, 3, 4, 5, 6], 4) == [0, 4]
    assert divisible_by([0], 4) == [0]
    assert divisible_by([1, 3, 5], 2) == []
    assert divisible_by([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("All tests passed.")