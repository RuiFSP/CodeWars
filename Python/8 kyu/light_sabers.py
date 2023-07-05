def how_many_light_sabers_do_you_own(name: str = "") -> int:
    """
    Returns the number of light sabers owned by a person.

    Args:
        name (str): The name of the person. Defaults to an empty string if not provided.

    Returns:
        int: The number of light sabers owned. Returns 18 if the name is "Zach", otherwise returns 0.
    """
    return 18 if name == "Zach" else 0


if __name__ == "__main__":
    assert how_many_light_sabers_do_you_own("Zach") == 18
    assert how_many_light_sabers_do_you_own("") == 0
    assert how_many_light_sabers_do_you_own("zach") == 0
    print("All tests passed!")
