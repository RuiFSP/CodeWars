def sum_cubes(n: int) -> int:
    """
    Returns the sum of the cubes of the first n natural numbers.
    """
    return sum([i**3 for i in range(1, n+1)])


if __name__ == "__main__":
    assert sum_cubes(3) == 36
    assert sum_cubes(5) == 225
    assert sum_cubes(10) == 3025
    print("All tests passed")