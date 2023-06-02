# You need to write regex that will validate a password to make sure it meets the following criteria:
#
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a digit
# only contains alphanumeric characters (note that '_' is not alphanumeric)


import re

# ^ asserts the start of the string.
# (?=.*[a-z]) is a positive lookahead assertion that checks if there is at least one lowercase letter.
# (?=.*[A-Z]) is a positive lookahead assertion that checks if there is at least one uppercase letter.
# (?=.*\d) is a positive lookahead assertion that checks if there is at least one digit.
# [a-zA-Z\d]{6,} matches any alphanumeric character (letter or digit) and ensures the password is at least six characters long.
# $ asserts the end of the string.


def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$'
    return re.match(pattern, password) is not None


if __name__ == "__main__":
    assert validate_password("fjd3IR9") is True
    assert validate_password("ghdfj32") is False
    assert validate_password("DSJKHD2") is False
    assert validate_password("dsF43") is False
    assert validate_password("4fdg5Fj3") is True
    print("All tests passed.")


