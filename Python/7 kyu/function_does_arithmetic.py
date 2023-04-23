def arithmetic(a, b, operator):
    operation = {
        "add": "+",
        "subtract": "-",
        "multiply": "*",
        "divide": "/"
    }

    print(operation[operator])
    print(type(operation[operator]))

    return eval(f"{a}{operation[operator]}{b}")


if __name__ == "__main__":
    assert arithmetic(1, 2, "add") == 3
    assert arithmetic(8, 2, "subtract") == 6
    assert arithmetic(5, 2, "multiply") == 10
    assert arithmetic(8, 2, "divide") == 4
    print("All tests passed!")

