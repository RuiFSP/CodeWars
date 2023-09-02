def power_of_two(n: int) -> bool:
    if n <= 0:
        return False
    
    # Check if there is only one bit set to 1
    return n & (n - 1) == 0

if __name__ == "__main__":
    assert power_of_two(0) == False
    assert power_of_two(1) == True
    assert power_of_two(2) == True
    assert power_of_two(5) == False
    assert power_of_two(6) == False
    assert power_of_two(4096) == True
    print("All tests passed")
