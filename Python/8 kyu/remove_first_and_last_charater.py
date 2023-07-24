def array(input_string: str) -> str:
    """
    Extracts the middle elements from a comma-separated string.

    Args:
        input_string (str): A comma-separated string containing elements.

    Returns:
        str: A string containing the middle elements separated by spaces.
             If the input string is empty or contains less than 3 elements, returns None.
    """
    if input_string == '':
        return None
    elements = input_string.split(',')
    if len(elements) < 3:
        return None
    return ' '.join(elements[1:-1])


if __name__ == "__main__":
    assert array('1,2,3') == '2'
    assert array('1,2,3,4') == '2 3'
    assert array('1,2,3,4,5') == '2 3 4'
    assert array('') is None
    assert array('1') is None
    assert array('1,2') is None
    print('All tests passed')

