def move_zeros(lst):
    return [x for x in lst if x != 0] + [x for x in lst if x == 0]


if __name__ == "__main__":
    assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    assert move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9,
                                                                                            9, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                            0, 0]
    assert move_zeros([0, 0]) == [0, 0]
    assert move_zeros([0]) == [0]
    assert move_zeros([]) == []
    print("All tests passed!")

