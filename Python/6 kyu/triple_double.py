import re

def triple_double(num1: int, num2: int) -> int:
    for digit in "0123456789":
        triple_pattern = re.compile(rf"{digit}{digit}{digit}")
        double_pattern = re.compile(rf"{digit}{digit}")

        if triple_pattern.search(str(num1)) and double_pattern.search(str(num2)):
            return 1

    return 0
    

if __name__ == "_main__":
    assert triple_double(451999277, 41177722899) == 1
    assert triple_double(1222345, 12345) == 0
    assert triple_double(12345, 12345) == 0
    assert triple_double(666789, 12345667) == 1
    assert triple_double(10560002, 100) == 1
    assert triple_double(1112, 122) == 0
    print("All tests passed")

