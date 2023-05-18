def get_age(age):
    return int(age[:2])


if __name__ == '__main__':
    assert get_age("2 years old") == 2
    assert get_age("4 years old") == 4
    assert get_age("5 years old") == 5
    assert get_age("9 years old") == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")