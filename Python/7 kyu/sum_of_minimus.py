def sum_of_minimums(numbers):
    return sum([number for arr in numbers for number in set(arr) if number == min(arr)])


if __name__ == "__main__":
    assert sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]]) == 9
    assert sum_of_minimums([[11, 12, 14, 54], [67, 89, 90, 56], [7, 9, 4, 3], [9, 8, 6, 7]]) == 76
    print("All tests passed!")
