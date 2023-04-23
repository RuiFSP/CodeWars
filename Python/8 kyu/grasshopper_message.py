def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"


if __name__ == '__main__':
    assert greet('Daniel', 'Daniel') == 'Hello boss'
    assert greet('Greg', 'Daniel') == 'Hello guest'
    print('Tests passed/')
