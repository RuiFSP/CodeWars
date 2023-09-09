import itertools

def get_even_numbers(arr: list) -> list:
    """
        Filters even numbers from a list.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list containing only the even numbers from the input list.
    """
    return list(itertools.filterfalse(lambda x: x % 2 != 0, arr))


if __name__ == "__main__":
        assert get_even_numbers([2,4,5,6]) == [2,4,6] #"Returned list is incorrect")
        assert get_even_numbers([]) == [] # "Returned list is incorrect")
        assert get_even_numbers([1]) == [] # "Returned list is incorrect")
        assert get_even_numbers([1,2]) == [2] #"Returned list is incorrect")
        assert get_even_numbers([1,2,3,4,5]) == [2,4]  #"Returned list is incorrect")
        assert get_even_numbers([2,4,6,8]) == [2,4,6,8] #"Returned list is incorrect")
        print("All tests passed")