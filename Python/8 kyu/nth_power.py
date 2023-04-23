def index(array, n):
    return array[n] ** n if n < len(array) else -1


if __name__ == '__main__':
    assert index([1, 2, 3, 4], 2) == 9
    assert index([1, 3, 10, 100], 3) == 1000000
    assert index([5, 6], 0) == 1
    print('Tests passed/')
