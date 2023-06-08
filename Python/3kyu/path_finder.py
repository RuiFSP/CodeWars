from heapq import heappop, heappush
from typing import List, Tuple

# You are at start location [0, 0] in mountain area of NxN and you can only move in one of the four cardinal
# directions (i.e. North, East, South, West). Return minimal number of climb rounds to target location [N-1, N-1].
# Number of climb rounds between adjacent locations is defined as difference of location altitudes
# (ascending or descending).
#
# Location altitude is defined as an integer number (0-9)

MOVES = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def path_finder(area: str) -> int:
    """
    Find the shortest path cost from the top-left corner to the bottom-right corner
    in the given area.

    Args:
        area (str): A string representing the area grid.

    Returns:
        int: The shortest path cost.

    """
    grid: List[List[int]] = [[int(j) for j in i] for i in area.split("\n")]
    edge: Tuple[int, int] = (len(grid) - 1, len(grid[0]) - 1)
    result: List[Tuple[int, Tuple[int, int]]] = [(0, (0, 0))]
    visited: set[Tuple[int, int]] = set()

    while result:
        cost, location = heappop(result)

        if location == edge:
            return cost
        elif location in visited:
            continue

        visited.add(location)
        for move in MOVES:
            row, col = location[0] + move[0], location[1] + move[1]
            if (
                    (row, col) not in visited
                    and (0 <= row <= edge[0] and 0 <= col <= edge[1])
            ):
                cost_new = cost + abs(grid[location[0]][location[1]] - grid[row][col])
                heappush(result, (cost_new, (row, col)))

    return 0


if __name__ == "__main__":
    a = "\n".join([
        "000",
        "000",
        "000"
    ])

    b = "\n".join([
        "010",
        "010",
        "010"
    ])

    c = "\n".join([
        "010",
        "101",
        "010"
    ])

    d = "\n".join([
        "0707",
        "7070",
        "0707",
        "7070"
    ])

    e = "\n".join([
        "700000",
        "077770",
        "077770",
        "077770",
        "077770",
        "000007"
    ])

    f = "\n".join([
        "777000",
        "007000",
        "007000",
        "007000",
        "007000",
        "007777"
    ])

    g = "\n".join([
        "000000",
        "000000",
        "000000",
        "000010",
        "000109",
        "001010"
    ])

    assert path_finder(a) == 0
    assert path_finder(b) == 2
    assert path_finder(c) == 4
    assert path_finder(d) == 42
    assert path_finder(e) == 14
    assert path_finder(f) == 0
    assert path_finder(g) == 4
