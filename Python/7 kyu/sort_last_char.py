def last(s:str) -> list:
    
    # Split the string into a list of words
    words = s.split()

    # Define a custom sorting key function
    def custom_key(word):
        return (word[-1], words.index(word))

    # Sort the words using the custom key
    sorted_words = sorted(words, key=custom_key)

    return sorted_words
    
if __name__ == "__main__":
    assert last("man i need a taxi up to ubud") == ["a", "need", "ubud", "i", "taxi", "man", "to", "up"]
    assert last("what time are we climbing up the volcano") == ["time", "are", "we", "the", "climbing", "volcano", "up", "what"]
    assert last("take me to semynak") == ["take", "me", "semynak", "to"]
    assert last("massage yes massage yes massage") == ["massage", "massage", "massage", "yes", "yes"]
    assert last("take bintang and a dance please") == ["a", "and", "take", "dance", "please", "bintang"]
    print("All tests passed")