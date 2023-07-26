def two_decimal_places(n: float) -> float:
    """
    Returns a float with two decimal places.
    """
    return round(n, 2)


if __name__ == "__main__":
    assert two_decimal_places(4.659725356) == 4.66
    assert two_decimal_places(173735326.37837326) == 173735326.38
    assert two_decimal_places(4.653725356) == 4.65
    print("All tests passed!")
