def count_stock(item: str) -> int:
    return int(item.split(" ")[1])

def strip_book(book_array: list) -> list:
    return [f"{item[0]} {count_stock(item)}" for item in book_array]

def stock_list(list_of_art: list, list_of_cat: list) -> str:
    my_dict = {}
    
    for item in strip_book(list_of_art):
        item_letter = item[0]
        if item_letter in my_dict:
            my_dict[item_letter] += count_stock(item)
        else:
            my_dict[item_letter] = count_stock(item)
    
    result = " - ".join([f"({cat} : {my_dict.get(cat, 0)})" for cat in list_of_cat])
    
    # Check if all stock counts are zero, return an empty string
    if all(value == 0 for value in my_dict.values()):
        return ""
    
    return result  

if __name__ == "__main__":
    b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B", "C", "D"]
    
    assert stock_list(b,c) == "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"
    
    
    e = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    f = ["A", "B"]
    assert stock_list(e,f) == "(A : 200) - (B : 1140)"
    
    print("All tests passed")