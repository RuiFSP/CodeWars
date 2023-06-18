def rgb(r: int, g: int, b: int) -> str:
    """
    Given three integers (r, g, b) representing the red, green, and blue
    components of a color, return the hex value of the color.

    Args:
        r (int): The red component of the color.
        g (int): The green component of the color.
        b (int): The blue component of the color.

    Returns:
        str: The hex value of the color.

    """
    return "".join(["{:02X}".format(max(min(x, 255), 0)) for x in [r, g, b]])


if __name__ == "__main__":
    assert rgb(0, 0, 0) == "000000"
    assert rgb(1, 2, 3) == "010203"
    assert rgb(255, 255, 255) == "FFFFFF"
    assert rgb(254, 253, 252) == "FEFDFC"
    assert rgb(-20, 275, 125) == "00FF7D"
    print("All tests passed successfully")