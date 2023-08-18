def in_asc_order(arr: list) -> bool:
    """
    Determine whether the numbers are in ascending order.
    An array is said to be in ascending order if there are no two adjacent
     integers where the left integer exceeds the right integer in value
    """
    return sorted(arr) == arr


if __name__ == "__main__":
    assert in_asc_order([1, 2]) == True
    assert in_asc_order([2, 1]) == False
    assert in_asc_order([1, 4, 13, 97, 508, 1047, 20058]) == True
    assert in_asc_order([56, 98, 123, 67, 742, 1024, 32, 90969]) == False
    print("All tests passed")
