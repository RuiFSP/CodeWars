def get_volume_of_cuboid(length: float, width: float, height: float) -> float:
    """
    Calculates the volume of a cuboid.

    Args:
        length (float): The length of the cuboid.
        width (float): The width of the cuboid.
        height (float): The height of the cuboid.

    Returns:
        float: The volume of the cuboid.

    """
    return length * width * height


if __name__ == "__main__":
    # Test cases
    assert get_volume_of_cuboid(1, 2, 2) == 4
    assert get_volume_of_cuboid(6.3, 2, 5) == 63
    print("All tests passed")
