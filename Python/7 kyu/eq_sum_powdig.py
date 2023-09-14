def eq_sum_powdig(hMax: int, exp: int) -> list:
    """
    Find numbers within a specified range that are equal to the sum of their digits raised to a given exponent.

    Args:
    hMax (int): The maximum number to check (inclusive).
    exp (int): The exponent to which each digit's power is raised.

    Returns:
    list: A list of numbers that meet the criteria.
    """
    result = []
    
    for i in range(10, hMax + 1):
        num_str = str(i)
        digit_sum = sum(int(digit) ** exp for digit in num_str)
        
        if digit_sum == i:
            result.append(i)
    
    return result



if __name__ == "__main__":
    assert eq_sum_powdig(100, 2) == []
    assert eq_sum_powdig(1000, 2) == []
    assert eq_sum_powdig(200, 3) == [153]
    assert eq_sum_powdig(370, 3) == [153, 370]
    print("All tests passed")