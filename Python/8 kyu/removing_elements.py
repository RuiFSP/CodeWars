def remove_every_other(my_list):
    return my_list[::2]


if __name__ == '__main__':
    assert remove_every_other([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert remove_every_other([5, 1, 2, 4, 1]) == [5, 2, 1]
    assert remove_every_other([1]) == [1]
    assert remove_every_other([]) == []
    assert remove_every_other(['Hello', 'Goodbye', 'Hello Again']) == ['Hello', 'Hello Again']
    assert remove_every_other([['Goodbye'], {'Great': 'Job'}]) == [['Goodbye']]
    print('Tests passed/')