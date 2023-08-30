def to_weird_case(s: str) -> str:
    """
        Accepts a string, and returns the same string with all even indexed characters in 
        each word upper cased, and all odd indexed characters in each word lower cased
    """
    words = s.split(' ')
    
    weird_words = []
    
    for word in words:
        weird_word = ''
        
        for index, char in enumerate(word):
            weird_word += char.upper() if index % 2 == 0 else char.lower()
        
        weird_words.append(weird_word)
    
    return ' '.join(weird_words)


if __name__ == "__main__":
    assert to_weird_case('This') == 'ThIs'
    assert to_weird_case('is') == 'Is'
    assert to_weird_case('THIs iS a TEST') == 'ThIs Is A TeSt'
    print("All tests passed")