def make_upper_case(s: str) -> str:
    """
    Given a string, return the same string but with all the characters
    in the string capitalized.
    :param s: string to be capitalized
    :return: capitalized string
    """
    return s.upper()


if __name__ == "__main__":
    assert make_upper_case("hello") == "HELLO"
    assert make_upper_case("hello world") == "HELLO WORLD"
    print("All tests passed successfully")