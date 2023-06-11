from typing import List


def delete_nth(order: List[int], max_e: int) -> List[int]:
    """
    Deletes elements from the order list if they occur more than max_e times.

    Args:
        order: A list of integers.
        max_e: Maximum number of occurrences allowed for each element.

    Returns:
        A new list with elements from order, excluding duplicates beyond max_e occurrences.
    """
    result = []
    occurrences = {}  # Dictionary to store the count of each element

    for num in order:
        if occurrences.get(num, 0) < max_e:
            result.append(num)
            occurrences[num] = occurrences.get(num, 0) + 1

    return result


if __name__ == "__main__":
    assert delete_nth([20, 37, 20, 21], 1) == [20, 37, 21]
    assert delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]
    print("All tests passed")
