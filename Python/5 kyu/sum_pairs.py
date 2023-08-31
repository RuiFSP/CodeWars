def sum_pairs(ints: list, s: int) -> list:
    """
    Given a list of integers and a single sum value, return the first two values (parse from the left please) 
    in order of appearance that add up to form the sum

    Args:
        ints (list): list of integers
        s (int): sum value

    Returns:
        list: the pair whose second element has the smallest index is the solution
    """
    cache = set()
    for number in ints:
        if s - number in cache:
            return [s - number, number]
        cache.add(number)


if __name__ == "__main__":
    assert sum_pairs([11, 3, 7, 5],10) == [3, 7]
    assert sum_pairs([4, 3, 2, 3, 4],6) == [4, 2]
    assert sum_pairs([10, 5, 2, 3, 7, 5],10) == [3,7]
    print("All tests passed")
    
    


