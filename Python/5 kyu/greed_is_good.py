from typing import List


def score(dice: List[int]) -> int:
    """
    Calculate the score for a given throw in the Greed dice game.

    Args:
        dice (List[int]): A list of five six-sided dice values.

    Returns:
        int: The total score for the throw.

    Raises:
        ValueError: If the length of the dice list is not equal to 5.
        ValueError: If any value in the dice list is not between 1 and 6.
    """

    if len(dice) != 5:
        raise ValueError("Invalid number of dice. Expected 5 dice.")

    for value in dice:
        if value < 1 or value > 6:
            raise ValueError("Invalid dice value. Values must be between 1 and 6.")

    print(f"dice is {dice}")

    # Initialize the score and count lists
    score = 0
    count = [0] * 6

    # Count the occurrences of each dice value
    for value in dice:
        count[value - 1] += 1

    # Calculate the score based on triplets
    for i in range(6):
        if count[i] >= 3:
            # Triplets of 1 have a special score of 1000
            if i == 0:
                score += 1000
            else:
                # For other values, the score is the value multiplied by 100
                score += (i + 1) * 100

            # Reduce the count of triplets from the count list
            count[i] -= 3

    # Calculate the score for remaining single dice values
    score += count[0] * 100  # Single 1s score 100 each
    score += count[4] * 50   # Single 5s score 50 each

    return score


if __name__ == "__main__":
    print("--- starting tests ---")
    print("--- test 1 ---")
    assert score([5, 1, 3, 4, 1]) == 250
    print("--- test 2 ---")
    assert score([1, 1, 1, 3, 1]) == 1100
    print("--- test 3 ---")
    assert score([2, 4, 4, 5, 4]) == 450
    print("--- test 4 ---")
    assert score([2, 3, 4, 6, 6]) == 0
    print("--- test 5 ---")
    assert score([4, 4, 4, 3, 3]) == 400
    print("All tests passed successfully")
