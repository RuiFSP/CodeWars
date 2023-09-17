def number_to_string(num:int) -> str:
    return str(num)


if __name__ == "__main__":
    assert number_to_string(67) == '67'
    assert number_to_string(79585) == '79585'
    assert number_to_string(79585) == "79585"
    assert number_to_string(1+2) == '3'
    assert number_to_string(1-2) == '-1'
    print("All tests passed")