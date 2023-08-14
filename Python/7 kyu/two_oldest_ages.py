def two_oldest_ages(ages: list) -> list:
    """
    Return two oldest ages (second-oldest, oldest)..

    :param ages: list of ages
    :return: two oldest ages in list, in order.
    """
    return sorted(ages)[-2:]


if __name__ == '__main__':
    assert two_oldest_ages([1, 5, 87, 45, 8, 8]) == [45, 87]
    assert two_oldest_ages([6, 5, 83, 5, 3, 18]) == [18, 83]
    assert two_oldest_ages([1, 5, 5, 2]) == [5, 5]
    assert two_oldest_ages([10, 1]) == [1, 10]
    print("All tests passed")
