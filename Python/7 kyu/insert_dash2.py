def insert_dash2(num: int) -> str:

    num_str = str(num)
    result = []

    for i in range(len(num_str) - 1):
        current_digit = int(num_str[i])
        next_digit = int(num_str[i + 1])

        if current_digit % 2 == 0 and next_digit % 2 == 0 and current_digit != 0 and next_digit != 0:
            result.append(str(current_digit) + '*')
        elif current_digit % 2 != 0 and next_digit % 2 != 0:
            result.append(str(current_digit) + '-')
        else:
            result.append(str(current_digit))

    result.append(num_str[-1])  # Add the last digit

    return ''.join(result)


if __name__ == "__main__":
    assert insert_dash2(454793) == "4547-9-3"
    assert insert_dash2(123456) == '123456'
    assert insert_dash2(40546793) == '4054*67-9-3'
    assert insert_dash2(1012356895) == '10123-56*89-5'
    assert insert_dash2(0) == '0'
    print("All tests passed")
