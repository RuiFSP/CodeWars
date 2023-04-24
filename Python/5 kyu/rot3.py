from string import ascii_lowercase, ascii_uppercase


def rot13(message):
    alphabet_lower = list(ascii_lowercase)
    alphabet_upper = list(ascii_uppercase)

    def rotate(c, alphabet):
        temp_c_index = alphabet.index(c)
        return alphabet[(temp_c_index + 13) % 26]

    return ''.join(
        rotate(c, alphabet_lower) if c.islower() else rotate(c, alphabet_upper) if c.isupper() else c for c in message)


if __name__ == "__main__":
    assert rot13('test') == 'grfg'
    assert rot13('Test') == 'Grfg'
    assert rot13('aA bB zZ 1234 *!?%') == 'nN oO mM 1234 *!?%'
    print('Tests passed/')
