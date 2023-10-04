""" 
Let’s use dictionarys to help us quickly convert Roman Numerals to integers. Take a 
look at this table to brush up on Roman Numerals. Do you notice any patterns we could take advantage of?

Specs
Write a function roman_to_int It should take one argument, a string, and convert it into its corresponding integer eg:

roman_to_int('IV') #=> 4
roman_to_int('XVI') #=> 16
roman_to_int('MI') #=> 1001 """


def roman_to_int(string:str) -> int:
    roman_dict = {
        "I": 1, 
        "V": 5, 
        "X": 10, 
        "L": 50, 
        "C": 100, 
        "D": 500, 
        "M": 1000
    }
    
    # Initialize variables to keep track of previous and total values
    prev_val = 0
    total = 0

    for char in string:
        # Get the integer value of the current Roman numeral
        current_val = roman_dict[char]
        total += current_val

        # Check if the current value is greater than the previous value
        if current_val > prev_val:
            # If it is, subtract twice the previous value from the total
            # This accounts for cases like IV (4) or IX (9)
            total -= 2 * prev_val

        # Update the previous value for the next iteration
        prev_val = current_val

    return total



if __name__ == "__main__":
    assert roman_to_int("IV") == 4
    assert roman_to_int("XII") == 12
    assert roman_to_int("XIV") == 14
    assert roman_to_int("XIX") == 19
    assert roman_to_int("XLIX") == 49
    assert roman_to_int("LXXVIII") == 78
    assert roman_to_int("LXXIX") == 79
    assert roman_to_int("CI") == 101
    assert roman_to_int("CDXCIX") == 499
    assert roman_to_int("MVI") == 1006
    assert roman_to_int("MCMLXXXIX") == 1989
    print("all tests passed")
    

