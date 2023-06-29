def alphanumeric(password: str) -> bool:
    """
    Check if a password consists only of alphanumeric characters.

    Args:
        password (str): The password to be checked.

    Returns:
        bool: True if the password is alphanumeric, False otherwise.
    """
    return password.isalnum()


if __name__ == '__main__':
    assert alphanumeric('Mazinkaiser') == True
    assert alphanumeric('hello world_') == False
    assert alphanumeric('PassW0rd') == True
    assert alphanumeric('     ') == False
    assert alphanumeric('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")