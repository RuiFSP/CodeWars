def queue_time(customers: list, n: int):
    if n == 1:
        return sum(customers)
    
    tills = [0] * n
    
    for customer in customers:
        min_till = min(tills)
        tills[tills.index(min_till)] += customer

    return max(tills)
    


if __name__ == "__main__":
    assert queue_time([], 1) == 0
    assert queue_time([5], 1) == 5
    assert queue_time([2], 5) == 2
    assert queue_time([1,2,3,4,5], 1) == 15
    assert queue_time([1,2,3,4,5], 100) == 5 
    assert queue_time([2,2,3,3,4,4], 2) == 9
    print("All tests passed")