def to_camel_case(text):
    if text == "":
        return text
    text = text.replace("-", "_")
    text = text.split("_")
    for i in range(1, len(text)):
        text[i] = text[i].capitalize()
    return "".join(text)


if __name__ == "__main__":
    assert to_camel_case("") == ""
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"
    print("All tests passed")