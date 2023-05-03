def scramble(s1, s2):
    for letter in set(s2):
        if s1.count(letter) < s2.count(letter):
            return False
    return True


if __name__ == "__main__":
    assert scramble("rkqodlw", "world") == True
    assert scramble("cedewaraaossoqqyt", "codewars") == True
    assert scramble("katas", "steak") == False
    assert scramble("scriptjava", "javascript") == True
    print("All tests passed successfully!")
