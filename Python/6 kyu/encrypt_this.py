def encrypt_this(text: str) -> str:
    """
    Encrypts the input text by applying a specific encryption algorithm.

    Args:
        text (str): The text to be encrypted.

    Returns:
        str: The encrypted text.

    """
    words = text.split()
    res = []
    for word in words:
        if len(word) == 1:
            res.append(str(ord(word[0])))
        elif len(word) == 2:
            res.append(str(ord(word[0])) + word[1])
        else:
            res.append(str(ord(word[0])) + word[-1] + word[2:-1] + word[1])
    return ' '.join(res)


if __name__ == '__main__':
    tests = [
        ("", ""),
        ("A wise old owl lived in an oak", "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
        ("The more he saw the less he spoke", "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
        ("The less he spoke the more he heard", "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
        ("Why can we not all be like that wise old bird",
         "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
        ("Thank you Piotr for all your help", "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"),
    ]

    for t in tests:
        inp, exp = t
        assert encrypt_this(inp) == exp
