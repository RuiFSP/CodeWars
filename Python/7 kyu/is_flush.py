def is_flush(cards:list) -> bool:
    first_suit = cards[0][-1]
    
    return all(card[-1] == first_suit for card in cards)

if __name__ == "__main__":
    assert is_flush(["AS", "3S", "9S", "KS", "4S"]) == True
    assert is_flush(["AD", "4S", "7H", "KC", "5S"]) == False
    assert is_flush(["AD", "4S", "10H", "KC", "5S"]) == False
    assert is_flush(["QD", "4D", "10D", "KD", "5D"]) == True
    print("All tests passed")