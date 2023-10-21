""" 
Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter words 
reversed (Just like the name of this Kata). Strings passed in will 
consist of only letters and spaces. Spaces will be included only 
when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test" 
"""


def spin_words(sentence:str) -> str:
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])


if __name__ == "__main__":
    assert spin_words("Welcome") == "emocleW"
    assert spin_words("to") == "to"
    assert spin_words("CodeWars") == "sraWedoC"
    assert spin_words("This is a test") == "This is a test"
    assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
    assert spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"
    print("All tests passed!")
