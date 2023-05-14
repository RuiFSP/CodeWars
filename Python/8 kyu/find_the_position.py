def position(alphabet):
    return f"Position of alphabet: {ord(alphabet) - 96}"


if __name__ == "__main__":
    assert(position("a") == "Position of alphabet: 1")
    assert(position("b") == "Position of alphabet: 2")
    assert(position("e") == "Position of alphabet: 5")
    assert(position("z") == "Position of alphabet: 26")
    print("All tests passed!")
