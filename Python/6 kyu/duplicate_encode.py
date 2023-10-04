""" 
The goal of this exercise is to convert a string to a new string where each character 
in the new string is "(" if that character appears only once in the original string, or ")" 
if that character appears more than once in the original string. Ignore capitalization when determining 
if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages.
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input! 
"""


def duplicate_encode(word:str) -> str:
    # Convert the word to lowercase
    word = word.lower()

    # Create a dictionary to store the counts of each letter using a dictionary comprehension
    letter_counts = {letter: word.count(letter) for letter in word}

    # Use a list comprehension to generate the result string
    result = ''.join([')' if letter_counts[letter] > 1 else '(' for letter in word])

    return result


def test_duplicate_encode():
    assert (duplicate_encode('din') == '((('), ('Success')
    assert (duplicate_encode('recede') == '()()()'), ('Success')
    assert (duplicate_encode('Success') == ')())())'), ('should ignore case')
    assert (duplicate_encode('(( @') == '))(('), ('should work with special characters')
    print('Tests passed')


if __name__ == "__main__":
    test_duplicate_encode()