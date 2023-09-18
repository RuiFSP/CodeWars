def define_suit(card:str)->str:
    
    suit_dict = {'C':'clubs',
                'D':'diamonds',
                'H':'hearts',
                'S':'spades'}
    
    return suit_dict[card[-1]]
        



assert define_suit('3C') == 'clubs'
assert define_suit('QS') == 'spades'
assert define_suit('9D') == 'diamonds'
assert define_suit('JH') == 'hearts'
print("All tests passed")
    