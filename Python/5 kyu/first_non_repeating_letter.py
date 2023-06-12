def first_non_repeating_letter(s: str) -> str:
    """
    Finds and returns the first non-repeating character in the given string.
    Returns an empty string if no such character is found.

    Args:
        s: The input string to search for the first non-repeating character.

    Returns:
        The first non-repeating character in the string, or an empty string if not found.
    """
    # Convert the input string to lowercase for case-insensitive comparison
    s_lower = s.lower()

    # Count the occurrences of each character in the string
    char_count = {}
    for c in s_lower:
        char_count[c] = char_count.get(c, 0) + 1

    # Find the first non-repeating character by iterating over the original string
    for i, c in enumerate(s):
        if char_count[s_lower[i]] == 1:
            return c

    return ""


if __name__ == "__main__":
    assert first_non_repeating_letter("a") == "a"
    assert first_non_repeating_letter("stress") == "t"
    assert first_non_repeating_letter("moonmen") == "e"
    assert first_non_repeating_letter("sTreSS") == "T"
    assert first_non_repeating_letter("") == ""
    assert first_non_repeating_letter("abba") == ""
    assert first_non_repeating_letter("aa") == ""
    assert first_non_repeating_letter("hello world, eh?") == "w"
    assert first_non_repeating_letter("sTreSS") == "T"
    print("All tests passed successfully")
