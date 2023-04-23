def plural(n):
    return n != 1


if __name__ == '__main__':
    assert plural(0) == True
    assert plural(1) == False
    assert plural(100) == True
    print('Tests passed/')
