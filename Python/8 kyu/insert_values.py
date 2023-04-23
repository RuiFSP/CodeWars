def invert(lst):
    return [-i for i in lst]


if __name__ == '__main__':
    assert list(invert([1, 2, 3, 4, 5])) == [-1, -2, -3, -4, -5]
    assert list(invert([1, -2, 3, -4, 5])) == [-1, 2, -3, 4, -5]
    assert list(invert([])) == []
    print('Tests passed/')
