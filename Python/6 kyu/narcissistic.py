def narcissistic(value: int) -> bool:
    """
    Check if a number is narcissistic.

    A Narcissistic Number is a number which is the sum of its own digits,
    each raised to the power of the number of digits in a given base.
    In this Kata, we will restrict ourselves to decimal (base 10).

    :param value: The number to check.
    :return: True if the number is narcissistic, False otherwise.
    """
    return value == sum([int(i) ** len(str(value)) for i in str(value)])


if __name__ == "__main__":
    assert narcissistic(7) == True
    assert narcissistic(371) == True
    assert narcissistic(122) == False
    assert narcissistic(4887) == False
    print("All tests passed")
