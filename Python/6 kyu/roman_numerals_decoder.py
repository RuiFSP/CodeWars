def solution(roman):
    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    prev_val = 0
    total = 0

    for char in roman:
        current_val = roman_dict[char]
        total += current_val

        if current_val > prev_val:
            total -= 2 * prev_val

        prev_val = current_val

    return total


if __name__ == "__main__":
    assert solution("I") == 1
    assert solution("II") == 2
    assert solution("III") == 3
    assert solution("IV") == 4
    assert solution("V") == 5
    assert solution("VI") == 6
    assert solution("VII") == 7
    assert solution("VIII") == 8
    assert solution("IX") == 9
    assert solution("X") == 10
    assert solution("XI") == 11
    assert solution("XIV") == 14
    assert solution("XV") == 15
    assert solution("XVI") == 16
    assert solution("XIX") == 19
    assert solution("XX") == 20
    assert solution("XXX") == 30
    assert solution("XL") == 40
    assert solution("L") == 50
    assert solution("LX") == 60
    assert solution("LXX") == 70
    assert solution("LXXX") == 80
    assert solution("XC") == 90
    assert solution("C") == 100
    assert solution("D") == 500
    assert solution("M") == 1000
    assert solution("MMM") == 3000
    assert solution("CMXCIX") == 999
    print('OK')
