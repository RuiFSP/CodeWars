from typing import List


def snail(snail_map: List[List[int]]) -> List[int]:
    """
    Generates a snail pattern from a given 2D map.

    Args:
        snail_map (List[List[int]]): The input 2D map.

    Returns:
        List[int]: The snail pattern generated from the map.
    """
    if not snail_map:
        return []

    print(f"\nInitial snail_map:{snail_map} \n")

    result = []
    while snail_map:
        result += snail_map.pop(0)
        # print(f"result: {result}")

        #  After the top row is processed, the remaining map is rotated counterclockwise by 90 degrees.
        #  The zip(*snail_map) part transposes the map by converting rows into columns and columns into rows.
        #  Then list() is used to convert the transposed map back into a list of rows. Finally, the [::-1]
        #  slicing notation is used to reverse the order of the rows. This rotation step prepares the map for the
        #  next iteration of the loop, effectively simulating moving inward along the spiral pattern
        snail_map = list(zip(*snail_map))[::-1]
        # print(f"remaining snail_map: {snail_map}")

    return result


if __name__ == "__main__":
    assert snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert snail([[1, 2, 3], [8, 9, 4], [7, 6, 5]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("All tests passed")
