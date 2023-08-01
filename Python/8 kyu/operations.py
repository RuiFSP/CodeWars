def add(a: int, b: int) -> int:
    return a + b


def subt(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    return a / b


def mod(a: int, b: int) -> int:
    return a % b


def exponent(a: int, b: int) -> int:
    return a ** b


if __name__ == "__main__":
    assert add(1, 2) == 3
    assert subt(1, 2) == -1
    assert multiply(1, 2) == 2
    assert divide(1, 2) == 0.5
    assert mod(1, 2) == 1
    assert exponent(1, 2) == 1
    print("All tests passed!")
