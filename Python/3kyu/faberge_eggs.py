# This solution fails for execution time:

def height_with_bad_execution_time(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + 1

    return dp[n][m]


# By using the concept of binomial coefficients and directly calculating the height without the need for
# dynamic programming or matrix storage, this solution achieves a more efficient execution time

def height(n, m):
    h, t = 0, 1
    for i in range(1, n + 1):
        # Update t using the formula for binomial coefficients
        t = t * (m - i + 1) // i
        # Accumulate t in h
        h += t
    # Return the calculated height
    return h


if __name__ == "__main__":
    assert height(0, 14) == 0
    assert height(2, 0) == 0
    assert height(2, 14) == 105
    assert height(7, 20) == 137979
    assert height(7, 500) == 1507386560013475
    assert height(237,
                  500) == 431322842186730691997112653891062105065260343258332219390917925258990318721206767477889789852729810256244129132212314387344900067338552484172804802659
    assert height(477,
                  500) == 3273390607896141870013189696827599152216642046043064789483291368096133796404674554883270092325904157150886684127420959866658939578436425342102468327399
    print("All Tests Passed")
