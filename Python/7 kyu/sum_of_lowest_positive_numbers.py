""" 
Create a function that returns the sum of the two lowest positive numbers given an array of
minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455. 
"""

def sum_two_smallest_numbers(numbers:list) -> int: 
    return sum(sorted(numbers)[:2])

if __name__ == "__main__":
    assert sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13
    assert sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13
    assert sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19
    assert sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19
    assert sum_two_smallest_numbers([25, 42, 12, 18, 22]) == 30
    assert sum_two_smallest_numbers([25, 42, 12, 18, 22]) == 30
    "All tests passed"
