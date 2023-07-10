def alphabet_position(text: str) -> str:
    """
    Returns the position of each letter in the alphabet as a string.

    The function converts the given text to lowercase and returns the position
    of each letter in the alphabet, separated by spaces. Non-alphabetic
    characters are ignored.

    Args:
        text (str): The input text.

    Returns:
        str: The positions of the alphabetic characters in the input text.

    """
    return " ".join([str(ord(c) - 96) for c in text.lower() if c.isalpha()])



if __name__ == "__main__":
    assert alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    assert alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
    print("All tests passed")
    print("You're a rock star.")