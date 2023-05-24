def duplicate_encode(word):
    # Convert the word to lowercase
    word = word.lower()

    # Initialize an empty string to store the result
    result = ""

    # Create a dictionary to store the counts of each letter
    letter_counts = {}

    # Count the occurrences of each letter in the word
    for letter in word:
        # Use the get() method to retrieve the count of a letter from letter_counts
        # If the letter is not in the dictionary, return 0 and add 1 to it
        # If the letter is already in the dictionary, return its value and add 1 to it
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    # Iterate over each letter in the word
    for letter in word:
        # If the count of the letter is greater than 1, add ')' to the result
        if letter_counts[letter] > 1:
            result += ")"
        # Otherwise, add '(' to the result
        else:
            result += "("

    # Return the final result
    return result


def test_duplicate_encode():
    assert (duplicate_encode('din') == '((('), ('Success')
    assert (duplicate_encode('recede') == '()()()'), ('Success')
    assert (duplicate_encode('Success') == ')())())'), ('should ignore case')
    assert (duplicate_encode('(( @') == '))(('), ('should work with special characters')
    print('Tests passed')


if __name__ == "__main__":
    test_duplicate_encode()