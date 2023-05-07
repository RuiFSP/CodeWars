def max_sequence(arr):
    if len(arr) == 0 or max(arr) < 0:
        return 0
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == "__main__":
    assert max_sequence([]) == 0
    assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]) == 0
    assert max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]) == 155
