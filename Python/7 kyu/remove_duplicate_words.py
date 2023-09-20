def remove_duplicate_words(s: str) -> str:
    
    unique_list = [] 
    [unique_list.append(word) for word in s.split() if word not in unique_list]
    return ' '.join(unique_list)


if __name__ == "__main__":
    assert remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta") == "alpha beta gamma delta"
    assert remove_duplicate_words("my cat is my cat fat") == "my cat is fat"
    print("All tests passed")
