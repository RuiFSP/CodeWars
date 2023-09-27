""" 
The Codewars Council meets at a circular table with n seats. Depending on the day d of the month, 
d people will be chosen as leaders of the council. These d leaders are spaced equidistantly from each other 
on the table, like spokes on a wheel. The leaders are chosen based on which grouping of d equidistant people 
have the largest summed honor. The honor of the participants for that day in the Council is given in an array 
arr of length n. Return the combined honor of the d leaders of the Council.

Given conditions -

    n % d == 0, ie. there will be no invalid cases. All groupings go fully around the circle.
    1 <= d <= 31, as you can't have 32 days in a month.
    n > 0 because you can't have a Council of 0 people. (You also can't have a table with 0 open seats, then it's just a nightstand or something)
    You can have negative honor on Codewars (but it is hard to do) and the solution may be negative.

Example -

[1, 2, 3, 4], 2 -> 6 because max(1+3, 2+4) == 6

[1, 5, 6, 3, 4, 2], 3 -> 11 because max(1+6+4, 5+3+2) == 11

[1, 1, 0], 1 -> 1 because max(1, 1, 0) == 1

Hint -

Something important to note is that you (usually) don't have to evaluate every sum in the array, as after n/d repetitions the sums loop over on themselves.
 """
import unittest

def largest_radial_sum(arr:list, d:int) -> int:
    n = len(arr)
    max_sum = float('-inf')

    for i in range(n):
        current_sum = 0

        for j in range(d):
            index = (i + j * (n // d)) % n  # Calculate the index of the person
            current_sum += arr[index]  # Add their honor to the current sum

        max_sum = max(max_sum, current_sum)  # Update the maximum sum if needed

    return max_sum


class TestLargest_RadialSum(unittest.TestCase):

    def test_sample_tests(self):
        
        sample_test_cases = [
            #   arr               d  expected
            ([1, 2, 3, 4],        2,    6),
            ([1, 5, 6, 3, 4, 2],  3,   11),
            ([1, 1, 0],           1,    1),
        ]
        
        for arr, d, expected in sample_test_cases:
            print(f'largest_radial_sum({arr}, {d})')
            self.assertEqual(largest_radial_sum(arr, d), expected)

if __name__ == '__main__':
    unittest.main()
