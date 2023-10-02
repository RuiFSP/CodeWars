# Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

# pyramid(0) => [ ]
# pyramid(1) => [ [1] ]
# pyramid(2) => [ [1], [1, 1] ]
# pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]

# Note: the subarrays should be filled with 1s

from itertools import repeat

def pyramid(n:int):
    # return [list(repeat(1,_)) if n > 0 else [] for _ in range(1,n+1)]
    return [[1]*x for x in range(1,n+1)]



if __name__ == "__main__":
    assert pyramid(0) == []
    assert pyramid(1) == [[1]]
    assert pyramid(2) == [[1], [1, 1]]
    assert pyramid(3) == [[1], [1, 1], [1, 1, 1]]
    print("All tests passed")
    