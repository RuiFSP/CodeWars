def filter_list(l):
    return [x for x in l if isinstance(x, (int, float))]


if __name__ == "__main__":
    assert filter_list([1, 2, 'a', 'b']) == [1, 2]
    assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15]
    assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]
    print("All tests passed!")
