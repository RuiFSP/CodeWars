def reverse_list(l):
    return l[::-1]


if __name__ == "__main__":
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_list([3, 1, 5, 4]) == [4, 5, 1, 3]
    assert reverse_list([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1]
    assert reverse_list([1]) == [1]
    print("All tests passed successfully")