def count_sheep(n):
    repeated_string = "{} sheep..."
    return "".join([repeated_string] * n).format(*[str(i + 1) for i in range(n)])


if __name__ == '__main__':
    assert count_sheep(1) == "1 sheep..."
    assert count_sheep(2) == "1 sheep...2 sheep..."
    assert count_sheep(3) == "1 sheep...2 sheep...3 sheep..."
    assert count_sheep(4) == "1 sheep...2 sheep...3 sheep...4 sheep..."
    print('Tests passed/')
