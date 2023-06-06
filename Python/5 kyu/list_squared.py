from math import sqrt
from typing import List, Optional, Union


def find_divisors(num: int) -> Optional[List[Union[int, int]]]:
    """
    Find divisors of a given number and check if the sum of their squares is a perfect square.

    Args:
        num: The number to find divisors for.

    Returns:
        A list containing the number and the sum of divisors' squares if the condition is met,
        otherwise returns None.
    """
    divisors = [i for i in range(1, int(sqrt(num) + 1)) if num % i == 0]
    divisors += [num // i for i in divisors if i != num // i]
    total = sum([x**2 for x in divisors])
    if sqrt(total).is_integer() and total > 0:
        return [num, total]
    return None


def list_squared(m: int, n: int) -> List[Optional[List[Union[int, int]]]]:
    """
    Find numbers within the given range whose divisors' squares sum up to a perfect square.

    Args:
        m: The lower bound of the range (inclusive).
        n: The upper bound of the range (inclusive).

    Returns:
        A list containing lists of numbers and their corresponding sums if the condition is met,
        otherwise returns an empty list.
    """
    output = [find_divisors(num) for num in range(m, n + 1) if find_divisors(num)]
    return output


def test_list_squared():
    assert list_squared(1, 250) == [[1, 1], [42, 2500], [246, 84100]]
    assert list_squared(42, 250) == [[42, 2500], [246, 84100]]
    assert list_squared(250, 500) == [[287, 84100]]
    print("All tests passed!")


if __name__ == "__main__":
    test_list_squared()
