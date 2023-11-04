"""
Complete the method which returns the number which is most frequent in the given input array. 
If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.
"""



def highest_rank(arr: list) -> int:
    
    count_dict = {}
    
    
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    
    max_count = max(count_dict.values())
    
    
    result = None
    
    
    for num, count in count_dict.items():
        if count == max_count:
            if result is None or num > result:
                result = num
    
    return result



if __name__ == "__main__":
    assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]) == 12
    assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]) == 10
                        