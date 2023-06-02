def no_odds(values):
    return [x for x in values if x % 2 == 0]


if __name__ == "__main__":
    assert no_odds([0, 1]) == [0]
    assert no_odds([0, 1, 2, 3]) == [0, 2]
    assert no_odds([1, 3, 5, 7, 9]) == []
    assert no_odds([0, 2, 4, 6, 8, 10]) == [0, 2, 4, 6, 8, 10]
    assert no_odds([2, 4, 8, 6, 0]) == [2, 4, 8, 6, 0]
    assert no_odds([]) == []
    print("All tests passed")
