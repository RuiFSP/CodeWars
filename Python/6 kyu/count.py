def count(s):
    """
    Counts the number of times each character appears in a string.
    """
    return {c: s.count(c) for c in s}


if __name__ == "__main__":
    assert count("aba") == {'a': 2, 'b': 1}
    assert count("abba") == {'a': 2, 'b': 2}
    assert count("abbba") == {'a': 2, 'b': 3}
    assert count("") == {}
    print("All tests successful")
