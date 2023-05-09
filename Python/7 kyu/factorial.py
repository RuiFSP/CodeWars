def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("n must be between 1 and 12")
    else:
        return 1 if n <= 1 else n * factorial(n - 1)


if __name__ == '__main__':
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(-1) == "n must be between 1 and 12"
    assert factorial(13) == "n must be between 1 and 12"
    print("All tests successful")
