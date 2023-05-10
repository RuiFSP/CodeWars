def spin_words(sentence):
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])


if __name__ == "__main__":
    assert spin_words("Welcome") == "emocleW"
    assert spin_words("to") == "to"
    assert spin_words("CodeWars") == "sraWedoC"
    assert spin_words("This is a test") == "This is a test"
    assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
    assert spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"
    print("All tests passed!")
