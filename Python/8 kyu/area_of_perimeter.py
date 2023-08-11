def area_or_perimeter(l: int, w: int) -> int:
    """
    Returns the area or perimeter of a rectangle
    :param l: length of rectangle
    :param w: width of rectangle
    :return: area or perimeter of rectangle
    """
    if l == w:
        return l * w
    else:
        return 2 * (l + w)


if __name__ == "__main__":
    assert area_or_perimeter(6, 10) == 32
    assert area_or_perimeter(4, 4) == 16
    print("All tests passed")
