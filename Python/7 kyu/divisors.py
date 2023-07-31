def divisors(n: int) -> str | list[int]:
    """
    Returns a list of all the divisors of an integer.
    """
    if n <= 1:
        raise ValueError("Input number must be greater than 1")

    divisors_list = [i for i in range(2, n) if n % i == 0]

    if not divisors_list:
        return f"{n} is prime"
    else:
        return divisors_list


if __name__ == "__main__":
    assert divisors(15) == [3, 5]
    assert divisors(253) == [11, 23]
    assert divisors(24) == [2, 3, 4, 6, 8, 12]
    assert divisors(25) == [5]
    assert divisors(13) == "13 is prime"
    assert divisors(3) == "3 is prime"
    assert divisors(29) == "29 is prime"
    print("All tests passed]")
