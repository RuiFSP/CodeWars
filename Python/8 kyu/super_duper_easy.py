def problem(a):
    return a * 50 + 6 if isinstance(a, (int, float)) else "Error"


if __name__ == '__main__':
    assert problem(1) == 56
    assert problem("hello") == "Error"
    print('Tests passed/')
