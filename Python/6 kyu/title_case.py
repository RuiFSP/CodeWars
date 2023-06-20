def title_case(title: str, minor_words: str = '') -> str:
    """
    Convert a given title to title case, excluding specified minor words.

    Args:
        title: The title string to convert.
        minor_words: A string containing minor words to exclude from capitalization. (default: '')

    Returns:
        The title string converted to title case.
    """
    title_words = title.lower().split()
    minor_words = minor_words.lower().split()

    for i in range(len(title_words)):
        if title_words[i] in minor_words and i != 0:
            title_words[i] = title_words[i]
        else:
            title_words[i] = title_words[i].capitalize()

    return ' '.join(title_words)


if __name__ == '__main__':
    assert title_case('') == ''
    assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
    assert title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows'
    assert title_case('the quick brown fox') == 'The Quick Brown Fox'
    print("All tests passed")