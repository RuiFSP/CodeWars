def litres(time: float) -> int:
    """
    Given time in hours, return the number of litres of water
    you should drink to stay hydrated.
    """
    return int(time * 0.5)


if __name__ == "__main__":
    assert litres(2) == 1
    assert litres(1.4) == 0
    assert litres(12.3) == 6
    assert litres(0.82) == 0
    assert litres(11.8) == 5
    assert litres(1787) == 893
    assert litres(0) == 0
    print("All tests passed")