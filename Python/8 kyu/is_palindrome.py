def is_palindrome(s: str) -> bool:
    return s.lower() == s.lower()[::-1]


if __name__ == "__main__":
    assert is_palindrome('a') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('Abba') == True
    assert is_palindrome('walter') == False
    assert is_palindrome('kodok') == True
    assert is_palindrome('Kasue') == False
    print("All tests Passed!")
