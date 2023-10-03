""" 
The distance formula can be used to find the distance between two points. 
What if we were trying to walk from point A to point B, but there were buildings 
in the way? We would need some other formula..but which?

Manhattan Distance
Manhattan distance is the distance between two points in a grid (like the grid-like 
street geography of the New York borough of Manhattan) calculated by only taking a vertical and/or horizontal path.

Complete the function that accepts two points and returns the Manhattan 
Distance between the two points.

The points are arrays or tuples containing the x and y coordinate in the grid. You can think of x as the row in the grid, and y as the column.

Examples
* Input [1, 1], [1, 1] => Output 0
* Input [5, 4], [3, 2] => Output 4
* Input [1, 1], [0, 3] => Output 3 
"""

def manhattan_distance(pointA: tuple, pointB:tuple) -> int:
    return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])


if __name__ == "__main__":
    assert manhattan_distance([1,1],[1,1]) == 0
    assert manhattan_distance([5,4],[3,2]) == 4
    assert manhattan_distance([1,1],[0,3]) == 3
    print("All tests passed")