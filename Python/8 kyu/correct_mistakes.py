def correct(s):
    my_conversion = {
        '5': 'S',
        '0': 'O',
        '1': 'I'
    }

    for i in range(len(s)):
        if s[i] in my_conversion:
            s = s[:i] + my_conversion.get(s[i]) + s[i + 1:]

    return s


if __name__ == '__main__':
    assert correct("L0ND0N") == "LONDON"
    assert correct("DUBL1N") == "DUBLIN"
    assert correct("51NGAP0RE") == "SINGAPORE"
    assert correct("BUDAPE5T") == "BUDAPEST"
    assert correct("PAR15") == "PARIS"