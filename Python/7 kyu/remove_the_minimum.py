def remove_smallest(numbers):
    if not numbers:
        return []

    updated_list = numbers.copy()
    print(updated_list)

    min_value_index = updated_list.index(min(updated_list))
    print(min_value_index)

    updated_list.pop(min_value_index)
    print(updated_list)

    return updated_list


if __name__ == '__main__':
    assert remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5]
    assert remove_smallest([5, 3, 2, 1, 4]) == [5, 3, 2, 4]
    assert remove_smallest([2, 2, 1, 2, 1]) == [2, 2, 2, 1]
    assert remove_smallest([]) == []
    print("All tests passed!")
