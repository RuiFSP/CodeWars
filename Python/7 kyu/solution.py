def solution(digits: str) -> int:
    """
    Given a string of digits, return the biggest possible 5-digit number
    that can be formed using those digits.

    :param digits: string of digits
    :return: biggest possible 5-digit number
    """
    digits = list(digits)
    greatest_sequence = 0
    for i in range(len(digits) - 4):
        sequence = int(''.join(digits[i:i+5]))
        if sequence > greatest_sequence:
            greatest_sequence = sequence
    return greatest_sequence


if __name__ == "__main__":
    assert solution('1234567898765') == 98765
    assert solution('731674765') == 74765
    print("All tests passed")