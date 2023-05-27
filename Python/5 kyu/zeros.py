def zeros(n):
    count = 0
    i = 5  # Trailing zeros are formed by multiples of 5 and its powers

    while n // i >= 1:
        count += n // i
        i *= 5

    return count


if __name__ == "__main__":
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
    print("All tests passed!")