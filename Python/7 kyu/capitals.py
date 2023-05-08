def capitals(word):
    return [i for i, letter in enumerate(word) if letter.isupper()]


if __name__ == "__main__":
    assert capitals("CodEWaRs") == [0, 3, 4, 6]
    assert capitals("abcdef") == []
    assert capitals("WZXZHDYDiISBXgNBMv") == [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16]
    print("All tests passed")
