def sequence_sum(begin_number, end_number, step):
    return sum([i for i in range(begin_number, end_number + 1, step)] if begin_number <= end_number else [])


if __name__ == "__main__":
    assert sequence_sum(2, 6, 2) == 12
    assert sequence_sum(1, 5, 1) == 15
    assert sequence_sum(1, 5, 3) == 5
    assert sequence_sum(0, 15, 3) == 45
    assert sequence_sum(16, 15, 3) == 0
    assert sequence_sum(2, 24, 22) == 26
    assert sequence_sum(2, 2, 2) == 2
    assert sequence_sum(1, 15, 3) == 35
    assert sequence_sum(15, 1, 3) == 0
    print("All tests passed!")

