def find_missing(sequence: list) -> int:

    n = len(sequence)
    
    # Calculate the common difference (d) between consecutive terms
    d = (sequence[-1] - sequence[0]) / n
    
    # Initialize the expected value as the first term
    expected = sequence[0]
    
    # Iterate through the list to find the missing term
    for i in range(n):
        if sequence[i] != expected:
            return int(expected)
        expected += d


if __name__ == "__main__":
    assert find_missing([1, 2, 3, 4, 6, 7, 8, 9]) == 5
    assert find_missing([1, 3, 4, 5, 6, 7, 8, 9]) == 2
    print("All tests passed")
