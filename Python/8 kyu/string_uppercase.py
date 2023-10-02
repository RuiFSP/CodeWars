"""
Is the string uppercase?
Task

Create a method to see whether the string is ALL CAPS.
Examples (input -> output)

"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True

In this Kata, a string is said to be in ALL CAPS whenever it does not
contain any lowercase letter so any string containing no letters at all is
trivially considered to be in ALL CAPS """

def is_uppercase(inp):
    return inp.upper() == inp

if __name__ == "__main__":
    assert is_uppercase("c") == False
    assert is_uppercase("C") == True
    assert is_uppercase("hello I AM DONALD") == False
    assert is_uppercase("HELLO I AM DONALD") == True
    assert is_uppercase("$%&") == True
    print("All tests passed")
