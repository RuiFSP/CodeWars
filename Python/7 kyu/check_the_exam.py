def check_exam(arr1, arr2):
    result = 0
    if len(arr1) == len(arr2) != 0:
        print("valid")
        for i in range(len(arr1)):
            if arr1[i] == arr2[i]:
                result += 4
            elif arr2[i] == "":
                result += 0
            else:
                result += -1
            print(f"the value added was {result}")

    else:
        print("not_valid")

    return 0 if result < 0 else result


if __name__ == "__main__":
    assert check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) == 6
    assert check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) == 7
    assert check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) == 16
    assert check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) == 0
    print("All tests passed!")