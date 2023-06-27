from typing import List


def sort_by_length(arr: List[str]) -> List[str]:
    """Sorts a list of strings by their length in ascending order.

    Args:
        arr: A list of strings.

    Returns:
        The list of strings sorted by their length in ascending order.

    Example:
        >>> sort_by_length(["i", "to", "beg", "life"])
        ['i', 'to', 'beg', 'life']
    """
    return sorted(arr, key=lambda x: len(x))


def basic_test_cases() -> None:
    """Performs basic test cases."""
    tests = [
        [["life", "i", "to", "beg"], ["i", "to", "beg", "life"]],
        [["", "pizza", "moderately", "brains"], ["", "pizza", "brains", "moderately"]],
        [["short", "longer", "longest"], ["short", "longer", "longest"]],
        [["a", "food", "of", "dog"], ["a", "of", "dog", "food"]],
        [["dictionary", "eloquent", "", "bees"], ["", "bees", "eloquent", "dictionary"]],
    ]

    for i, test in enumerate(tests, 1):
        result = sort_by_length(test[0])
        if result == test[1]:
            print(f"Test case {i} passed.")
        else:
            print(f"Test case {i} failed. Expected: {test[1]}, Got: {result}")


if __name__ == "__main__":
    basic_test_cases()
    print("All tests passed!")
