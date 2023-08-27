def thirt(n: int) -> int:
    pattern = [1, 10, 9, 12, 3, 4]
    n_str = str(n)
    n_len = len(n_str)
    total = 0

    for i in range(n_len):
        total += int(n_str[n_len - 1 - i]) * pattern[i % 6]

    if total == n:
        return total
    else:
        return thirt(total)


if __name__ == "__main__":
    assert thirt(8529) == 79
    assert thirt(5634) == 57
    assert thirt(85299258) == 31
    assert thirt(1111111111) == 71
    assert thirt(987654321) == 30
    print("All tests passed")
