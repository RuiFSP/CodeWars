def sum_digits(number):
    return sum(int(digit) for digit in str(number) if digit.isdigit())


if __name__ == "__main__":
    assert sum_digits(10) == 1
    assert sum_digits(99) == 18
    assert sum_digits(-32) == 5
    assert sum_digits(123456789) == 45
    assert sum_digits(0) == 0
    print("All tests passed!")
