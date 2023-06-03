def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def gap(g, m, n):
    prev_prime = None
    for num in range(m, n + 1):
        if is_prime(num):
            if prev_prime is not None and num - prev_prime == g:
                return [prev_prime, num]
            prev_prime = num
    return None


if __name__ == "__main__":
    assert gap(2, 100, 110) == [101, 103]
    assert gap(4, 100, 110) == [103, 107]
    assert gap(6, 100, 110) == None
    assert gap(8, 300, 400) == [359, 367]
    assert gap(10, 300, 400) == [337, 347]
    assert gap(2, 100, 103) == [101, 103]
    print("All tests passed")
