def take(arr: list,n: int)-> list:
    return arr[:n]


if __name__ == "__main__":
    assert take([0, 1, 2, 3, 5, 8, 13], 3) == [0, 1, 2]
    print("All tests passed")