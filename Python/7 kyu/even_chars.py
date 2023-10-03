""" 
Write a function that returns a sequence (index begins with 1) of all the 
even characters from a string. If the string is smaller than two characters 
or longer than 100 characters, the function should return "invalid string".

For example:

"abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
"a"             --> "invalid string" 
"""

def even_chars(st:str) -> list:
    
    if (len(st) < 2 or len(st) > 100):
        return "invalid string"
    
    return [c for i,c in enumerate(st) if i % 2 != 0]
   
    # cool aternative with slicing: return list(st[1::2]) if 2<=len(st)<=100 else "invalid string" 
    
if __name__ == "__main__":
    assert even_chars("a") == "invalid string"
    assert even_chars("abcdefghijklm") == ["b", "d", "f", "h", "j", "l"]
    assert even_chars("aBc_e9g*i-k$m") == ["B", "_", "9", "*", "-", "$"]
    print("All tests passed")