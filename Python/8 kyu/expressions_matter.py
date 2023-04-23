def expression_matter(a, b, c):
    comb_1 = a * (b * c)
    comb_2 = a * b * c
    comb_3 = a + b * c
    comb_4 = (a + b) * c
    comb_5 = a + b + c
    comb_6 = a * (b + c)

    return max(comb_1, comb_2, comb_3, comb_4, comb_5, comb_6)


if __name__ == '__main__':
    assert expression_matter(2, 1, 2) == 6
    assert expression_matter(2, 1, 1) == 4
    assert expression_matter(1, 1, 1) == 3
    assert expression_matter(1, 2, 3) == 9
    assert expression_matter(1, 3, 1) == 5
    assert expression_matter(2, 2, 2) == 8
    assert expression_matter(5, 1, 3) == 20
    assert expression_matter(3, 5, 7) == 105
    assert expression_matter(5, 6, 1) == 35
    assert expression_matter(1, 6, 1) == 8
    assert expression_matter(2, 6, 1) == 14
    assert expression_matter(6, 7, 1) == 48
    assert expression_matter(2, 10, 3) == 60
    assert expression_matter(1, 8, 3) == 27
    assert expression_matter(9, 7, 2) == 126
    assert expression_matter(1, 1, 10) == 20
    print('Tests passed/')
