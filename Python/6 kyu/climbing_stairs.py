def climbing_stairs(cost: list) -> int:
    n = len(cost)
    
    # Initialize dp array
    dp = [0] * n
    
    # Initialize dp[0] and dp[1]
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    # Fill dp array using dynamic programming
    for i in range(2, n):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    
    # Return the minimum cost to reach the top
    return min(dp[-1], dp[-2])    


if __name__ == "__main__":
    assert climbing_stairs([10, 15, 20]) == 15
    assert climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert climbing_stairs([0, 2, 2, 1]) == 2
    assert climbing_stairs([0, 2, 3, 2]) == 3
    assert climbing_stairs([0, 0, 0, 0, 0, 0]) == 0
    print("All tests passed")