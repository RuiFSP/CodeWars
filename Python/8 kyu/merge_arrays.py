from typing import List


def merge_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Merges two sorted arrays into a single sorted array in ascending order.

    Args:
        arr1 (List[int]): The first sorted array.
        arr2 (List[int]): The second sorted array.

    Returns:
        List[int]: The merged and sorted array without duplicates.
    """
    return sorted(set(arr1 + arr2))


if __name__ == "__main__":
    assert merge_arrays([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_arrays([1, 3, 5, 7, 9], [10, 8, 6, 4, 2]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert merge_arrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12]) == [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]
    print("All tests passed")
