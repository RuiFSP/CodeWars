import math


def lcm(a, b):
    """Return the least common multiple of two integers."""
    return abs(a * b) // math.gcd(a, b)


def convert_fracts(lst):
    """Convert a list of fractions to equivalent fractions with a common denominator."""
    if not lst:
        # If the list is empty, return an empty list.
        return []
    else:
        # Set the initial denominator to the denominator of the first fraction.
        d = lst[0][1]
        # Iterate over the remaining fractions and compute the LCM of their denominators.
        for _, y in lst[1:]:
            d = lcm(d, y)
        # Return a list of equivalent fractions with the common denominator.
        return [[x * d // y, d] for x, y in lst]


if __name__ == '__main__':
    assert convert_fracts([[1, 2], [1, 3], [1, 4]]) == [[6, 12], [4, 12], [3, 12]]
    print('Tests passed/')