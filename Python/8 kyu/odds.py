odds = lambda lst: list(filter(lambda x: x % 2 != 0, lst))


if __name__ == '__main__':
    assert odds([]) == []
    assert odds([2, 4, 6]) == []
    assert odds([1, 3, 5]) == [1, 3, 5]
    assert odds([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
    print("All tests passed successfully")
