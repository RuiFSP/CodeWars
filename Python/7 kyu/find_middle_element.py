def gimme(input_array):
    return input_array.index(sorted(input_array)[1])


if __name__ == "__main__":
    assert gimme([2, 3, 1]) == 0
    assert gimme([5, 10, 14]) == 1
    print("All tests passed!")