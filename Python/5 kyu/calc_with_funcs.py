def number(n):
    def func(operation=None):
        return operation(n) if operation else n
    return func


zero, one, two, three, four, five, six, seven, eight, nine = [number(n) for n in range(10)]


def plus(x): return lambda y: y + x
def minus(x): return lambda y: y - x
def times(x): return lambda y: y * x
def divided_by(x): return lambda y: y // x


if __name__ == '__main__':
    assert (seven(times(five())) == 35)
    assert (four(plus(nine())) == 13)
    assert (eight(minus(three())) == 5)
    assert (six(divided_by(two())) == 3)
    print('All tests passed!')
