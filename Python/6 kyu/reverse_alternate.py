# Reverse every other word in a given string, then return the string. Throw away any leading or trailing 
# whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be 
# treated as if they are a part of the word in this kata.

def reverse_alternate(s:str)-> str:
    result = []
    for i,v in enumerate(s.split()):
        if i % 2 == 0:
            result.append(v)
        else:
            result.append(v[::-1])
            
    return ' '.join(result)

if __name__ == "__main__":
    assert reverse_alternate("Did it work?") == "Did ti work?"
    assert reverse_alternate("I really hope it works this time...") == "I yllaer hope ti works siht time..."
    assert reverse_alternate("Reverse this string, please!") == "Reverse siht string, !esaelp"
    assert reverse_alternate("Have a beer") == "Have a beer"
    assert reverse_alternate("   ") == ""
    assert reverse_alternate("This is not a test ") == "This si not a test"
    assert reverse_alternate("This       is a  test ") == "This si a tset"
    print("All tests passed")