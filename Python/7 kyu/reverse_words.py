def reverse_words(string: str) -> str:
    """
    Reverses the order of words in a given string.

    Args:
        string: The input string.

    Returns:
        The reversed string where each word is reversed.
    """
    return ' '.join([word[::-1] for word in string.split()])


if __name__ == '__main__':
    assert reverse_words('Hello World!') == 'olleH !dlroW'
    print('All tests passed successfully!')