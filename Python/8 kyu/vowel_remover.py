def shortcut(s):
    vowels = set('aeiou')
    return ''.join(c for c in s if c not in vowels)


if __name__ == '__main__':
    assert shortcut('codewars') == 'cdwrs'
    assert shortcut('goodbye') == 'gdby'
    assert shortcut('HELLO WORLD!!!') == 'HELLO WORLD!!!'
    assert shortcut('aeiou') == ''
    assert shortcut('') == ''
    print('tests passed')
