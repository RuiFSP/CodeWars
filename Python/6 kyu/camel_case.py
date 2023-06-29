def camel_case(s: str) -> str:
    """
    Convert string to camel case
    :param s: string
    :return: camel case string
    """
    if s == '':
        return s
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    return ''.join(s)


if __name__ == '__main__':
    assert camel_case('test case') == 'TestCase'
    assert camel_case('camel case method') == 'CamelCaseMethod'
    assert camel_case('say hello ') == 'SayHello'
    assert camel_case(' camel case word') == 'CamelCaseWord'
    assert camel_case('') == ''
    print("All tests passed")
