def are_you_playing_banjo(name: str) -> str:
    """
    Determine if a person plays banjo based on the starting letter of their name.
    
    Args:
        name (str): Name of the person.

    Returns:
        str: A phrase indicating whether the person plays banjo.
    """
    if name and name[0].lower() == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"



if __name__ == "__main__":
    assert are_you_playing_banjo("martin") == "martin does not play banjo"
    assert are_you_playing_banjo("Rikke") == "Rikke plays banjo"
    assert are_you_playing_banjo("bravo") == "bravo does not play banjo"
    assert are_you_playing_banjo("rolf") == "rolf plays banjo"
    print("all tests passed")

