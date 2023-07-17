from typing import List


def find_missing_letter(chars: List[str]) -> str:
    """
    Find the missing letter in a list of consecutive letters.

    Args:
        chars (List[str]): List of characters in ascending order.

    Returns:
        str: The missing letter in the sequence.
    """

    for i in range(len(chars) - 1):
        if ord(chars[i + 1]) - ord(chars[i]) != 1:
            return chr(ord(chars[i]) + 1)


if __name__ == "__main__":
    assert find_missing_letter(['a', 'b', 'c', 'd', 'f']) == 'e'
    assert find_missing_letter(['O', 'Q', 'R', 'S']) == 'P'
    print("All tests passed successfully")
