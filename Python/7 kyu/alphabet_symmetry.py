def solve(arr: list) -> list:
    """
    Calculate the number of letters that are the same position in each word.

    Args:
        arr (list): List of words.

    Returns:
        list: List of numbers of letters that are the same position in each word.
    """

    results = []

    for word in arr:
        count = 0
        for i, char in enumerate(word):
            alphabet_index = ord(char.lower()) - ord('a')
            if alphabet_index == i:
                count += 1
        results.append(count)

    return results


if __name__ == "__main__":
    assert solve(["abode", "ABc", "xyzD"]) == [4, 3, 1]
    assert solve(["abide", "ABc", "xyz"]) == [4, 3, 0]
    assert solve(["IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"]) == [6, 5, 7]
    assert solve(["encode", "abc", "xyzD", "ABmD"]) == [1, 3, 1, 3]
    print("Well done! Go check your code")
