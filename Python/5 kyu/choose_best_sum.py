import itertools
from typing import List, Optional


def choose_best_sum(t: int, k: int, ls: List[int]) -> Optional[int]:
    """
    Find the largest sum of k integers from the given list that does not exceed t.

    Args:
        t (int): The maximum sum allowed.
        k (int): The number of integers to choose.
        ls (List[int]): The list of integers.

    Returns:
        Optional[int]: The largest sum of k integers that does not exceed t.
                       Returns None if no such sum exists.
    """
    sums = (sum(combination) for combination in itertools.combinations(ls, k))
    sums2 = (s for s in sums if s <= t)
    return max(sums2, default=None)


if __name__ == "__main__":
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
    assert choose_best_sum(230, 4, xs) == 230
    assert choose_best_sum(430, 5, xs) == 430
    assert choose_best_sum(430, 8, xs) is None
