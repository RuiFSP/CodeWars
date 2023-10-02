"""
Challenge - Colorful Algorithm

Background and Objectives

We can break a number into different contiguous sub-subsequence parts.
For example, the number 324 can be broken into parts like (3, 2, 4, 32, 24, 324)
. A colorful number is a number where the products of all the subsets of
the digits are different. eg:

263 is a colorful number (2, 6, 3, 2x6, 6x3, 2x6x3) are all different
236 is not (2, 3, 6, 2x3, 3x6, 2x3x6) has 6 twice (6 and 2x3)
Specs

We want you to write a function is_colorful which takes a single number as
an argument and returns True if the number is colorful, False otherwise.

For this exercise, only consider numbers with up to 3 digits (not more), eg:
is_colorful(263) #=> True
is_colorful(236) #=> False
"""

def is_colorful(num):
    # Convert the number to a string to work with its digits
    num_str = str(num)
    length = len(num_str)

    # Create a set to store unique products
    unique_products = set()

    # Handle single-digit numbers
    if length == 1:
        return True

    # Iterate through the digits and generate all possible subsequences
    for i in range(length):
        for j in range(i + 1, length + 1):
            subsequence = num_str[i:j]
            print(subsequence)
            product = 1

            # Calculate the product of the digits in the subsequence
            for digit in subsequence:
                product *= int(digit)

            # If the product is already in the set, it's not colorful
            if product in unique_products:
                return False

            # Add the product to the set
            unique_products.add(product)

    # If all products are unique, the number is colorful
    return True

if __name__ == "__main__":
    # assert is_colorful(263) == True
    # assert is_colorful(236) == False
    # assert is_colorful(122) == False
    # assert is_colorful(1) == True
    # assert is_colorful(0) == True
    assert is_colorful(112233) == False
    print("All tests passed")
