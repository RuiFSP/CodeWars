def howmuch(m: int,n: int) -> list:
    """
    Find possible values of fortune, car cost, and boat cost based on given conditions.

    Args:
    m (int): The lower bound of the range for possible fortunes.
    n (int): The upper bound of the range for possible fortunes.

    Returns:
    list: A list of lists containing the possible values of fortune, boat cost, and car cost.
          Each inner list is in the format ["M: f", "B: b", "C: c"].
    """
    
    
    results = []
    for f in range(min(m, n), max(m, n) + 1):
        if (f - 1) % 9 == 0 and (f - 2) % 7 == 0:
            c = (f - 1) // 9
            b = (f - 2) // 7
            results.append(["M: {}".format(f), "B: {}".format(b), "C: {}".format(c)])
    return results



if __name__ == "__main__":
     assert howmuch(1, 100) == [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]]
     assert howmuch(1000, 1100) == [["M: 1045", "B: 149", "C: 116"]]
     assert howmuch(10000, 9950) == [["M: 9991", "B: 1427", "C: 1110"]]
     assert howmuch(0, 200) == [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]]
     assert howmuch(2950, 2950) ==  []
     assert howmuch(20000, 20100) == [["M: 20008", "B: 2858", "C: 2223"], ["M: 20071", "B: 2867", "C: 2230"]]
     print("All tests passed")