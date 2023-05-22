def encode(st):
    return st.translate(str.maketrans('aeiou', '12345'))


def decode(st):
    return st.translate(str.maketrans('12345', 'aeiou'))


if __name__ == '__main__':
    assert encode('hello') == 'h2ll4'
    assert encode('How are you today?') == 'H4w 1r2 y45 t4d1y?'
    assert encode('This is an encoding test.') == 'Th3s 3s 1n 2nc4d3ng t2st.'
    assert decode('h2ll4') == 'hello'
    print('All tests passed.')
