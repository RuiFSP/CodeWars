from typing import Union


def sum_mul(n: int, m: int) -> Union[int, str]:
    """
    Calculates the sum of all multiples of n below m (excluding m).

    Args:
        n (int): The number whose multiples need to be calculated.
        m (int): The upper limit, excluding this number from the multiples.

    Returns:
        Union[int, str]: The sum of multiples if the input is valid, otherwise "INVALID".
    """
    if not isinstance(n, int) or not isinstance(m, int) or n <= 0 or m <= 0:
        return "INVALID"

    multiples_sum = 0
    for num in range(n, m, n):
        multiples_sum += num

    return multiples_sum


if __name__ == "__main__":
    assert sum_mul(0, 0) == 'INVALID'
    assert sum_mul(2, 9) == 20
    assert sum_mul(4, -7) == 'INVALID'
    print("All tests passed!")
