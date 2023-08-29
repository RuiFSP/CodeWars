def parts_sums(ls: list) -> list:
    cumulative_sum = sum(ls)  # Calculate the sum of the entire list
    result = [cumulative_sum]  # Initialize the result list with the sum of the entire list
    
    for num in ls:
        cumulative_sum -= num  # Subtract the current element from the cumulative sum
        result.append(cumulative_sum)  # Append the new cumulative sum to the result list
    
    return result

def basic_tests():
    tests = [
        ([], [0]),
        ([0, 1, 3, 6, 10], [20, 20, 19, 16, 10, 0]),
        ([1, 2, 3, 4, 5, 6], [21, 20, 18, 15, 11, 6, 0]),
        ([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358], [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0])
        ]
    
    for x in tests:
        assert parts_sums(x[0]) == x[1]
    
        

if __name__ == "__main__":
    basic_tests()
    print("All tests passed")