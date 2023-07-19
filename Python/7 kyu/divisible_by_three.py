def divisible_by_three(st: str) -> bool:
    """
    Checking if a number is divisible by 3
    """
    digits_sum = sum(map(int, st))

    if digits_sum < 10:
        return digits_sum in (0, 3, 6, 9)

    return divisible_by_three(str(digits_sum))


if __name__ == '__main__':
    assert divisible_by_three("123") == True
    assert divisible_by_three("19254") == True
    assert divisible_by_three("88") == False
    assert divisible_by_three("1") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
