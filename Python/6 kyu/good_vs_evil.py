def good_vs_evil(good: str, evil: str) -> str:
    """Calculate the result of a battle between good and evil armies.

    Args:
        good (str): The representation of the good army's forces.
        evil (str): The representation of the evil army's forces.

    Returns:
        str: The result of the battle.

    """
    good_list = [1, 2, 3, 3, 4, 10]
    evil_list = [1, 2, 2, 2, 3, 5, 10]
    good_sum = sum([int(good.split()[i - 1]) * good_list[i - 1] for i in range(1, len(good_list) + 1)])
    evil_sum = sum([int(evil.split()[i - 1]) * evil_list[i - 1] for i in range(1, len(evil_list) + 1)])
    if good_sum > evil_sum:
        return "Battle Result: Good triumphs over Evil"
    elif good_sum < evil_sum:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"


if __name__ == "__main__":
    assert good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1') == "Battle Result: Evil eradicates all trace of Good"
    assert good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0') == "Battle Result: Good triumphs over Evil"
    assert good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0') == "Battle Result: No victor on this battle field"
    print("All tests passed successfully")