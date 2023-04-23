def double_integer(i):
    return i * 2


if __name__ == '__main__':
    assert double_integer(2) == 4
    assert double_integer(4) == 8
    assert double_integer(-10) == -20
    assert double_integer(0) == 0
    assert double_integer(100) == 200
    print('Tests passed/')