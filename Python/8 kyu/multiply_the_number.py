def multiply(n: int) -> int:    
    return n * 5**len(str(abs(n)))


if __name__ == "__main__":
    assert multiply(10) == 250
    assert multiply(5) == 25
    assert multiply(200) == 25000
    assert multiply(0) == 0
    assert multiply(-2) == -10
    print("All tests passed")