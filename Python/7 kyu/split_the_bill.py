def split_the_bill(x: dict) -> dict:
    """
    Calculate how much each person should pay or receive based on the amount they spent.

    Args:
        x (dict): A dictionary with names as keys and the amount spent by each person as values.

    Returns:
        dict: A dictionary with the same names as keys and the amount each person should pay or receive as values.
             The amounts are rounded to two decimal places.
    """
    total_spent = sum(x.values())
    num_people = len(x)
    avg_cost = total_spent / num_people
    
    return {name : round(amount - avg_cost, 2) for name, amount in x.items()}


if __name__ == "__main__":
    assert split_the_bill({'A': 20, 'B': 15, 'C': 10}) == {'A': 5, 'B': 0, 'C': -5}
    assert split_the_bill({'A': 40, 'B': 25, 'X': 10}) == {'A': 15, 'B': 0, 'X': -15}
    print("All tests passed")