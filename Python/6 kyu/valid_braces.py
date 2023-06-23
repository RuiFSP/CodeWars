from typing import Dict


def valid_braces(string: str) -> bool:
    """Check if the braces in the string are valid.

    Args:
        string: A string containing braces.

    Returns:
        True if the braces are valid, False otherwise.
    """
    braces: Dict[str, str] = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack = []
    for char in string:
        if char in braces:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if braces[stack.pop()] != char:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    # Test cases
    assert valid_braces("()") == True
    assert valid_braces("[(])") == False
    assert valid_braces("(){}[]") == True
    assert valid_braces("([{}])") == True
    assert valid_braces("([{}])[]") == True
    assert valid_braces("([{}])[]()") == True
    assert valid_braces("([{}])[](){}") == True
    assert valid_braces("([{}])[](){}()") == True
    print("All tests passed successfully")
