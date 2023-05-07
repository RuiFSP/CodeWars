def check_multiple(num):
    return num % 3 == 0 or num % 5 == 0


def solution(number):
    return False if number < 0 else sum([i for i in range(number) if check_multiple(i)])


if __name__ == "__main__":
    assert solution(4) == 3
    assert solution(6) == 8
    assert solution(16) == 60
    assert solution(3) == 0
    assert solution(5) == 3
    assert solution(15) == 45
    assert solution(0) == 0
    assert solution(-1) == 0
    assert solution(10) == 23
    assert solution(20) == 78
    assert solution(200) == 9168
    print("All tests passed.")
