def min_value(digits):
    return int(''.join(map(str, sorted(set(digits)))))


if __name__ == "__main__":
    assert min_value([1, 3, 1]) == 13
    assert min_value([4, 7, 5, 7]) == 457
    assert min_value([4, 8, 1, 4]) == 148
    print("Success)")