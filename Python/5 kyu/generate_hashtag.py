def generate_hashtag(s: str) -> str:
    """
    Generates a hashtag from the given string.

    Args:
        s (str): The input string.

    Returns:
        str: The generated hashtag.

    Raises:
        ValueError: If the input string is empty or exceeds 140 characters.
    """
    if len(s) > 140 or len(s) == 0:
        return False

    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    hashtag = '#' + ''.join(capitalized_words)

    return hashtag


if __name__ == "__main__":
    assert generate_hashtag('Codewars') == '#Codewars'
    assert generate_hashtag('Codewars      ') == '#Codewars'
    assert generate_hashtag('      Codewars') == '#Codewars'
    assert generate_hashtag('Codewars is nice') == '#CodewarsIsNice'
    assert generate_hashtag('Codewars is nice ') == '#CodewarsIsNice'
    assert generate_hashtag('codewars is nice') == '#CodewarsIsNice'
    assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'
    assert generate_hashtag('codewars is nice ') == '#CodewarsIsNice'
    assert generate_hashtag('c i n') == '#CIN'
    assert generate_hashtag('codewars  is  nice') == '#CodewarsIsNice'
    assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') == False
    assert generate_hashtag('') == False
    print("All tests passed")