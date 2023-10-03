""" 
Kevin is noticing his space run out! Write a function that removes the spaces 
from the values and returns an array showing the space decreasing.
For example, running this function on the array ['i', 'have','no','space'] 
would produce ['i','ihave','ihaveno','ihavenospace'] 
"""

def spacey(array:list) -> list:
    
    # end_result = []
    
    # for i in range(len(array)):
    #     end_result.append(''.join(array[:i + 1]))
    #     print(end_result)
        
    # return end_result

    return ["".join(array[:i + 1]) for i in range(len(array))]

if __name__ == "__main__":
    assert spacey(['kevin', 'has','no','space']) == [ 'kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace']
    assert spacey(['this','cheese','has','no','holes']) == ['this','thischeese','thischeesehas','thischeesehasno','thischeesehasnoholes']
    print("All tests passed")