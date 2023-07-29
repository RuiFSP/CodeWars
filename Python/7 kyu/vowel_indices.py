def vowel_indices(word:  str) -> list[int]:
    """
    Return a list of indices of the vowels in a word.
    """
    vowels = 'aeiouy'
    indices = []
    for i, c in enumerate(word):
        if c.lower() in vowels:
            indices.append(i + 1)
    return indices


if __name__ == "__main__":
    assert vowel_indices('mmm') == []
    assert vowel_indices('apple') == [1, 5]
    assert vowel_indices('123456') == []
    assert vowel_indices('UNDISARMED') == [1, 4, 6, 9]
    assert vowel_indices('bialy') == [2, 3, 5]
    print("All tests passed!")
