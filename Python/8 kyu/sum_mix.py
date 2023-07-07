from typing import List


def sum_mix(arr: List[str]) -> int:
    """
    Calculates the sum of array values treating all elements as numbers.

    Args:
        arr (List[str]): The input array of integers as strings and numbers.

    Returns:
        int: The sum of the array values as if all were numbers.
    """
    total_sum = 0
    for num in arr:
        if isinstance(num, str):
            try:
                num = int(num)
            except ValueError:
                try:
                    num = float(num)
                except ValueError:
                    continue
        total_sum += num
    return total_sum


if __name__ == "__main__":
    assert sum_mix([9, 3, '7', '3']) == 22
    assert sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]) == 42
    assert sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']) == 41
    assert sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']) == 45
    assert sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]) == 61
    print("All Tests Passed")
