def anagram_difference(word1: str, word2: str) -> int:
    """
    Counts the number of letters that need to be removed from two words to make them anagrams.

    Args:
        word1 (str): The first word (lowercase only).
        word2 (str): The second word (lowercase only).

    Returns:
        int: The number of letters to remove.

    Example:
        anagram_difference('code wars', 'hacker rank') => 10
    """
    # Convert the words to lowercase and remove any non-alphabetic characters
    word1 = ''.join(c for c in word1 if c.islower())
    word2 = ''.join(c for c in word2 if c.islower())

    # Create dictionaries to store the frequency of each letter in the words
    letter_freq1 = {}
    letter_freq2 = {}

    # Count the frequency of letters in word1
    for letter in word1:
        letter_freq1[letter] = letter_freq1.get(letter, 0) + 1

    # Count the frequency of letters in word2
    for letter in word2:
        letter_freq2[letter] = letter_freq2.get(letter, 0) + 1

    # Calculate the number of letters to remove
    removal_count = 0

    # Iterate over the letters in word1 and compare their frequencies with word2
    for letter in letter_freq1:
        if letter in letter_freq2:
            removal_count += abs(letter_freq1[letter] - letter_freq2[letter])
        else:
            removal_count += letter_freq1[letter]

    # Iterate over the letters in word2 that are not in word1 and add their frequencies to the removal count
    for letter in letter_freq2:
        if letter not in letter_freq1:
            removal_count += letter_freq2[letter]

    return removal_count


sample_test_cases = (
    ('', '', 0),
    ('a', '', 1),
    ('', 'a', 1),
    ('ab', 'a', 1),
    ('ab', 'ba', 0),
    ('ab', 'cd', 4),
    ('codewars', 'hackerrank', 10)
)


def tests():
    for w1, w2, expected in sample_test_cases:
        assert anagram_difference(w1, w2) == expected, f"anagram_difference({w1!r}, {w2!r})"


if __name__ == "__main__":
    tests()
    print('All tests passed.')
