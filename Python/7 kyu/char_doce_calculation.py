def calc(x: str) -> int:
    
    total1 = ''.join([str(ord(letter)) for letter in x])
    total2 = total1.replace('7','1')
    
    return sum([int(n) for n in total1]) - sum([int(n) for n in total2])

    #alternative
    # total1 = ''.join(map(lambda c: str(ord(c)), x))
    # total2 = total1.replace('7', '1')
    # return sum(map(int, total1)) - sum(map(int, total2))

if __name__ == "__main__":
    assert calc('abcdef') == 6
    assert calc('ifkhchlhfd') == 6
    assert calc('aaaaaddddr') == 30
    assert calc('jfmgklf8hglbe') == 6
    assert calc('jaam') == 12
    print("All tests passed")
