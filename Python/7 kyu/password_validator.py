""" 
Your job is to create a simple password validation function, as seen on many websites.

The rules for a valid password are as follows:

There needs to be at least 1 uppercase letter.
There needs to be at least 1 lowercase letter.
There needs to be at least 1 number.
The password needs to be at least 8 characters long.
You are permitted to use any methods to validate the password.

Examples:
password("Abcd1234"); ===> true
password("Abcd123"); ===> false
password("abcd1234"); ===> false
password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"); ===> true
password("ABCD1234"); ===> false
password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,"); ===> true;
password("!@#$%^&*()-_+={}[]|\:;?/>.<,"); ===> false;
Extra info
You will only be passed strings.
The string can contain any standard keyboard character.
Accepted strings can be any length, as long as they are 8 characters or more. 
"""

import re

def password(s: str) -> bool:
    # Check if the password is at least 8 characters long
    if len(s) < 8:
        return False

    # Check for at least 1 uppercase letter
    if not re.search(r'[A-Z]', s):
        return False

    # Check for at least 1 lowercase letter
    if not re.search(r'[a-z]', s):
        return False

    # Check for at least 1 number
    if not re.search(r'[0-9]', s):
        return False

    return True


if __name__ == "__main__":
    assert password("Abcd1234") == True
    assert password("Abcd123") == False
    assert password("abcd1234") == False
    assert password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890") == True
    assert password("ABCD1234") == False
    assert password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,") == True
    assert password("!@#$%^&*()-_+={}[]|\:;?/>.<,") == False
    assert password("") == False
    assert password(" aA1----") == True
    assert password("4aA1----") == True
    print("All tests passed")