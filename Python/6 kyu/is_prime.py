def is_prime(num:  int) -> bool:
    """
    Returns True if num is prime, False otherwise
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


if __name__ == "__main__":
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(73) == True
    assert is_prime(75) == False
    assert is_prime(-1) == False
    print("All tests passed")
