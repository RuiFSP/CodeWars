""" 
Thanks to Pythons built in random library we have access to a shuffle method, which when 
called on a list - returns a shuffled version of that list. In this advanced exercise, lets 
try to code a shuffle function ourselves from scratch.

Specs
Code a manual_shuffle function:

The function should take one argument, a list, and return a new list with all the items of 
your original list in a new, randomized order
Do Not use any built in list methods to manipulate the order such as sort()
Do Not use the built in shuffle method in pythons random library (lets do it the hard way). 
But you might find some other helpful methods in there, we imported the random library for you at the top of the file 😉
Hint: You should not makes changes to the original List, the copy method will come in handy. 
ne approach could be to create a new empty array B, and until A is empty, randomly select an index in A, 
append the element in A at that index into B, then delete that index in A. Proceed until A is empty. B should contain the new shuffled array! 
"""

import random

def manual_shuffle(array:list) -> list:
    
    temp_array = array.copy()
    print(f"My copy of original array is: {temp_array}")
    result = []
    
    # checking for different memory llocation to avoid mutability of original array
    # print(id(array))
    # print(id(temp_array))
    
    
    while len(temp_array) > 0:
        
        #picking at random from my choice array
        a = random.choices(temp_array)[0]
        print(f"my random choice from array is {a}")
        
        #remove element form my temporary array
        temp_array.remove(a)
        
        # verify that is smaller
        print(f"my copy array has now {len(temp_array)} elements")
        
        #add that element to my result array
        result.append(a)
        print(f"My Array has: {result}")
        

    return result

if __name__ == "__main__":
    
    assert len(manual_shuffle(list(range(10)))) == 10
    assert manual_shuffle(list(range(100))) != manual_shuffle(list(range(100)))
    assert set(manual_shuffle(list(range(100)))) == set(range(100))
    print("All tests passed")
