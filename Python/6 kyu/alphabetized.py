def alphabetized(s):
    # remove whitespace and punctuation
    s = ''.join(filter(str.isalpha, s))

    # create a histogram of the characters in the input string
    hist = {}
    for char in s:
        char_lower = char.lower()
        hist[char_lower] = hist.get(char_lower, '') + char

    # iterate through the alphabet to create the output string
    new_string = ''
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in hist:
            new_string += hist[char]

    return new_string


if __name__ == "__main__":
    assert alphabetized("") == ""
    assert alphabetized(" ") == ""
    assert alphabetized(" a") == "a"
    assert alphabetized("a ") == "a"
    assert alphabetized("A b B a") == "AabB"
    assert alphabetized("!@$%^&*()_+=-`,") == ""
    assert alphabetized("The Holy Bible") == "BbeehHilloTy"
    assert alphabetized("CodeWars can't Load Today") == "aaaaCcdddeLnooorstTWy"
    print("All tests passed. Well done!")
