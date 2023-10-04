""" 
Pirates have notorious difficulty with enunciating. They tend to blur all the letters together
and scream at people.

At long last, we need a way to unscramble what these pirates are saying.

Write a function that will accept a jumble of letters as well as a dictionary, 
and output a list of words that the pirate might have meant.

For example:

grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
Should return ["sport", "ports"].

Return matches in the same order as in the dictionary. Return an empty array if
there are no matches.

Good luck! 
"""

from collections import Counter

def grabscrab(said: str, possible_words: list) -> list:
    said_counter = Counter(said)
    return [word for word in possible_words if len(word) == len(said) and all(said_counter[letter] >= count for letter, count in Counter(word).items())]




if __name__ == "__main__":
    
    assert grabscrab("trisf", ["first"]) == ["first"]
    assert grabscrab("oob", ["bob", "baobab"]) == []
    assert grabscrab("ainstuomn", ["mountains", "hills", "mesa"]) == ["mountains"]
    assert grabscrab("oolp", ["donkey", "pool", "horse", "loop"]) == ["pool", "loop"]
    assert grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]) == ["sport", "ports"]
    assert grabscrab("ourf", ["one", "two", "three"]) == []
    assert grabscrab("racer", ["crazer", "carer", "racar", "caers", "racer"]) == ["carer", "racer"]
    assert grabscrab("abba", ["aabb", "abcd", "bbaa", "abbb", "aaab"]) == ["aabb", "bbaa"]
    assert grabscrab("owrdl", ['old', 'different', 'about', 'eye', 'duolw', 'for', 'leave', 'would', 'bad', 'next', 'into', 'number', 'all']) == ['old', 'duolw', 'would']
    print("All tests passed")
    