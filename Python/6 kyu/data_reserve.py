def data_reverse(data: list) -> list:
    chunk_size = 8
    reversed_data = []

    for i in range(0, len(data), chunk_size):
        chunk = data[i:i+chunk_size]
        reversed_data = chunk + reversed_data

    return reversed_data



if __name__ == "__main__":
    
    data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
    data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
    assert data_reverse(data1) == data2
    
    data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
    data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
    assert data_reverse(data3) == data4
    
    print("All tests passed")