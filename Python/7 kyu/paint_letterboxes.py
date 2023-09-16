def paint_letterboxes(start: int, finish: int):
    
    digit_frequency = [0] * 10

    for num in range(start, finish + 1):
        num_str = str(num)
        
        for digit in num_str:
            digit_frequency[int(digit)] += 1
    
    return digit_frequency

if __name__ == "__main__":
    assert paint_letterboxes(125, 132) == [1,9,6,3,0,1,1,1,1,1]
    print("All tests passed")