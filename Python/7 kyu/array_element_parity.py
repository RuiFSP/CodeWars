def solve(arr):
    return [el for el in arr if -el not in arr][0]

    #cool solution
    sum(set(arr))

if __name__ == "__main__":
    assert solve([1, -1, 2, -2, 3]) == 3
    assert solve([-3, 1, 2, 3, -1, -4, -2]) == -4
    assert solve([1, -1, 2, -2, 3, 3]) == 3
    assert solve([-9, -105, -9, -9, -9, -9, 105]) == -9
    assert solve([-110, 110, -38, -38, -62, 62, -38, -38, -38]) == -38
    
    print("All assertions passed.")
