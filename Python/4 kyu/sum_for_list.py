from collections import defaultdict
from math import sqrt


# Returns a list of prime factors of n
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors


# Returns a list of pairs [p, sum of all ij of I for which p is a prime factor (p positive) of ij]
def sum_for_list(arr):
    # Determine all the prime factors of the absolute values of the numbers in the input array
    factors = set()
    for num in arr:
        factors.update(prime_factors(abs(num)))

    # Calculate the sum of all the numbers in the array that are divisible by each factor
    factor_sums = defaultdict(int)
    for num in arr:
        for factor in factors:
            if num % factor == 0:
                factor_sums[factor] += num

    # Return the result as a list of pairs, sorted by increasing order of the prime factors
    result = [[factor, factor_sums[factor]] for factor in sorted(factors)]
    return result


if __name__ == '__main__':
    assert sum_for_list([12, 15]) == [[2, 12], [3, 27], [5, 15]]
    assert sum_for_list([15, 21, 24, 30, 45]) == [[2, 54], [3, 135], [5, 90], [7, 21]]
    print('All tests passed.')
