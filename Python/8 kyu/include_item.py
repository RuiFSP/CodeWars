from typing import List


def include(arr: List[int], item: int) -> bool:
    """
    Check if an item is included in the given list.

    Args:
        arr (List[int]): The list to search for the item.
        item (int): The item to search for in the list.

    Returns:
        bool: True if the item is found in the list, False otherwise.
    """
    return item in arr


if __name__ == "__main__":
    assert include([1, 2, 3, 4], 3) == True
    assert include([1, 2, 4, 5], 3) == False
    print("All tests passed")
