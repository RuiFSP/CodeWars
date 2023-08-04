def even_numbers(arr: list, n: int) -> list:
    """
        Return the first n even numbers from the array
    Args:
        arr: list of numbers
        n: number of even numbers to return
    Returns:
        list of first n even numbers from the array
    """
    return [i for i in arr if i % 2 == 0][-n:]


if __name__ == "__main__":
    assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [4, 6, 8]
    assert even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) == [-8, 26]
    assert even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) == [6]
    print("Coding complete? Click 'Check' to earn cool rewards!")
