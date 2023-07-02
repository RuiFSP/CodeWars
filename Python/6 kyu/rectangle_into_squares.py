from typing import List, Optional


def sq_in_rect(length: int, width: int) -> Optional[List[int]]:
    """
    Divides a "true" rectangle into squares of decreasing size.

    Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.

    Returns:
        Optional[List[int]]: A list containing the sizes of each square, or None if the dimensions are the same.
    """
    if length == width:
        return None

    sizes = []
    while length and width:
        side = min(length, width)
        sizes.append(side)
        if length == side:
            width -= side
        else:
            length -= side
    return sizes


if __name__ == "__main__":
    assert sq_in_rect(5, 5) is None
    assert sq_in_rect(5, 3) == [3, 2, 1, 1]
    assert sq_in_rect(3, 5) == [3, 2, 1, 1]
    assert sq_in_rect(20, 14) == [14, 6, 6, 2, 2, 2]
    print("All tests Passed!")
