def lovefunc(flower1: int, flower2: int) -> bool:
    """
    Determine if they are in love, if one of the flowers has an even number of petals 
    and the other has an odd number of petals it means they are in love.
    
    Args:
        flower1 (int): Number of petals of flower 1.
        flower2 (int): Number of petals of flower 2.

    Returns:
        bool: True if they are in love, False otherwise.
    """
    return (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0)

if __name__ == "__main__":
    assert lovefunc(1,4) == True
    assert lovefunc(2,2) == False
    assert lovefunc(0,1) == True
    assert lovefunc(0,0) == False
    print("All tests passed")