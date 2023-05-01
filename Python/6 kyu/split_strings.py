def solution(s):
    # Append "_" to s if its length is odd
    if len(s) % 2 != 0:
        s += "_"

    # Use list comprehension to create the pairs
    return [s[i:i + 2] for i in range(0, len(s), 2)]


if __name__ == "__main__":
    assert solution("asdfadsf") == ['as', 'df', 'ad', 'sf']
    assert solution("asdfads") == ['as', 'df', 'ad', 's_']
    assert solution("") == []
    assert solution("x") == ["x_"]
    assert solution("xy") == ["xy"]
    print('Tests passed/')

