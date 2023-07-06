from typing import List


def add_length(string: str) -> List[str]:
    """
    Adds the length of each word to the end of the word and returns them as an array.

    Args:
        string: A string containing words separated by spaces.

    Returns:
        A list of modified words with the length appended to each element.
    """
    words = string.split()
    result = []

    for word in words:
        word_length = str(len(word))
        result.append(word + ' ' + word_length)

    return result


if __name__ == "__main__":
    assert add_length('apple ban') == ["apple 5", "ban 3"]
    assert add_length('you will win') == ["you 3", "will 4", "win 3"]
    assert add_length('you') == ["you 3"]
    assert add_length('y') == ["y 1"]
    print("All tests passed!")
