def multiplication_table(size):
    return [[row * column for column in range(1, size+1)] for row in range(1, size+1)]


if __name__ == '__main__':
    assert (multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
