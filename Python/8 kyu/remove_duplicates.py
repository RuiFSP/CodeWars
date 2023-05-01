def distinct(seq):
    unique_list = []
    for x in seq:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


if __name__ == '__main__':
    assert distinct([1]) == [1]
    assert distinct([1, 2, 3]) == [1, 2, 3]
    assert distinct([1, 1, 2, 2, 3]) == [1, 2, 3]
    assert distinct([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert distinct([1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert distinct([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert distinct([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert distinct([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]) == [1, 2, 3, 4, 5, 6, 7]
    print('Tests passed/')
