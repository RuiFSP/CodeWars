def alphabet_war(battlefield: str) -> str:
    """
    Accepts a battlefield string and returns the letters that survived the nuclear strike.

    The battlefield string consists of only small letters, #, [, and ].
    The nuclear shelter is represented by square brackets []. The letters inside the square brackets represent letters inside the shelter.
    The # means a place where a nuclear strike hit the battlefield. If there is at least one # on the battlefield, all letters outside of the shelter die.
    When there is no # on the battlefield, all letters survive.
    If there are 2 or more # hits close to a shelter, the shelter is destroyed, and all letters inside evaporate.

    Args:
        battlefield (str): The battlefield string.

    Returns:
        str: The letters that survived the nuclear strike.
    """
    if '#' not in battlefield:
        return battlefield.replace('[', '').replace(']', '')

    shelter_arr = []
    strike_num = 0
    shelter_str = ''
    shelter_flag = False

    for idx, char in enumerate(battlefield):
        if char == '#':
            strike_num += 1
        elif char == '[':
            shelter_arr.append(strike_num)
            strike_num = 0
            shelter_flag = True
            shelter_str = ''
        elif char == ']':
            shelter_arr.append(shelter_str)
            shelter_flag = False
        else:
            if shelter_flag:
                shelter_str += char

    shelter_arr.append(strike_num)

    return ''.join(item for idx, item in enumerate(shelter_arr) if
                   isinstance(item, str) and shelter_arr[idx - 1] + shelter_arr[idx + 1] < 2)


if __name__ == "__main__":
    assert alphabet_war('[a]#[b]#[c]') == 'ac'
    assert alphabet_war('[a]#b#[c][d]') == 'd'
    assert alphabet_war('[a][b][c]') == 'abc'
    assert alphabet_war('##a[a]b[c]#') == 'c'
    assert alphabet_war('abde[fgh]ijk') == 'abdefghijk'
    assert alphabet_war('ab#de[fgh]ijk') == 'fgh'
    assert alphabet_war('ab#de[fgh]ij#k') == ''
    assert alphabet_war('##abde[fgh]ijk') == ''
    assert alphabet_war('##abde[fgh]') == ''
    assert alphabet_war('##abcde[fgh]') == ''
    assert alphabet_war('abcde[fgh]') == 'abcdefgh'
    assert alphabet_war('##abde[fgh]ijk[mn]op') == 'mn'
    assert alphabet_war('#abde[fgh]i#jk[mn]op') == 'mn'
    assert alphabet_war('[ab]adfd[dd]##[abe]dedf[ijk]d#d[h]#') == 'abijk'
    print("All tests passed successfully!")
