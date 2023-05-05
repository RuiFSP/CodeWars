import math


def solution(a):
    # find the GCD of all numbers in the list
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = math.gcd(gcd, a[i])

    # return the smallest possible sum
    return gcd * len(a)


if __name__ == "__main__":
    assert solution([9]) == 9
    assert solution([6, 9, 21]) == 9
    assert solution([1, 21, 55]) == 3
    print("All tests passed successfully")
