def number_to_pwr(number: int, p: int) -> int:
    if p == 0:
        return 1
    return number * number_to_pwr(number, p - 1)


if __name__ == "__main__":
    assert number_to_pwr(4, 2) == 16
    assert number_to_pwr(10, 4) == 10000
    assert number_to_pwr(10, 0) == 1
    print("All tests passed")
