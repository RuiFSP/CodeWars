def show_sequence(n: int) -> str:
    """
    Returns the sum of the first n integers as a string.
    """
    if n < 0:
        return f"{n}<0"
    elif n == 0:
        return "0=0"
    else:
        return f"{'+'.join(str(i) for i in range(0, n + 1))} = {sum(range(n+1))}"


if __name__ == "__main__":
    assert show_sequence(6) == "0+1+2+3+4+5+6 = 21"
    assert show_sequence(7) == "0+1+2+3+4+5+6+7 = 28"
    assert show_sequence(0) == "0=0"
    assert show_sequence(-1) == "-1<0"
    assert show_sequence(-10) == "-10<0"
    print("All tests passed successfully!")
