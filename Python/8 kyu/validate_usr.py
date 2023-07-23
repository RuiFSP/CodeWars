import re


def validate_usr(username: str) -> bool:
    """
    Validates the username using a regular expression.

    The username must meet the following criteria:
    - Contains only lowercase letters, numbers, or underscores.
    - Has a length between 4 and 16 characters (both inclusive).

    Parameters:
        username (str): The username to be validated.

    Returns:
        bool: True if the username is valid, False otherwise.
    """
    pattern = r"^[a-z0-9_]{4,16}$"
    return bool(re.match(pattern, username))


if __name__ == "__main__":
    assert validate_usr("asddsa") == True
    assert validate_usr("a") == False
    assert validate_usr("Hass") == False
    assert validate_usr("Hasd_12assssssasasasasaasasasas") == False
    assert validate_usr("") == False
    assert validate_usr("____") == True
    assert validate_usr("012") == False
    assert validate_usr("p1pp1") == True
    assert validate_usr("asd43 34") == False
    assert validate_usr("asd43_34") == True
    print("All tests passed.")
