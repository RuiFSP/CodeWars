def parse(data: str) -> list:
    """
    Parse a string of operations and return a list of values based on the given operations.

    Args:
        data (str): A string containing a sequence of operations to be performed.

    Returns:
        list: A list of values obtained by applying the operations in the input string.
    """
    my_list = []
    temp_val = 0
    
    operations = {
        'o': lambda x: my_list.append(x),
        'i': lambda x: x + 1,
        's': lambda x: x * x,
        'd': lambda x: x - 1,
    }
    
    for letter in data:
        print(f"Currently my array is: {my_list}")
        if letter in operations:
            if letter == 'o':
                operations[letter](temp_val)
            else:
                temp_val = operations[letter](temp_val)
        else:
            print("finished parsing")
    
    print(f"Final array is {my_list}")
    return my_list
    


if __name__ == "__main__":
    assert parse("ooo")==[0,0,0]    
    assert parse("ioioio")==[1,2,3]
    assert parse("idoiido")==[0,1]
    assert parse("isoisoiso")==[1,4,25]
    assert parse("codewars")==[0]
    print("All tests passed")
