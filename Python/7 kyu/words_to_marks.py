def words_to_marks(s: str) -> int:
    """
    Given a string, return the sum of the ASCII values of each character in the string.
    """
    return sum([ord(x) - 96 for x in s])


if __name__ == "__main__":
    assert words_to_marks("attitude") == 100
    assert words_to_marks("friends") == 75
    assert words_to_marks("family") == 66
    assert words_to_marks("selfness") == 99
    assert words_to_marks("knowledge") == 96
    print("All tests passed")
