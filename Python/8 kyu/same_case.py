def same_case(a:  str, b: str) -> int:
    """
    Returns 1 if the two characters are the same case,
    0 if they are not the same case,
    and -1 if either of the characters is not a letter.
    """
    if a.isalpha() and b.isalpha():
        return 1 if a.isupper() == b.isupper() else 0
    return -1


if __name__ == "__main__":
    assert same_case('C', 'B') == 1
    assert same_case('b', 'a') == 1
    assert same_case('d', 'd') == 1
    assert same_case('A', 's') == 0
    assert same_case('c', 'B') == 0
    assert same_case('b', 'Z') == 0
    assert same_case('\t', 'Z') == -1
    assert same_case('H', ':') == -1
    print("All tests passed successfully!")
