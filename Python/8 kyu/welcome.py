def greet(language):
    my_db = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }

    message = my_db.get(language)

    return message if message is not None else 'Welcome'


if __name__ == '__main__':
    assert greet('english') == 'Welcome'
    assert greet('dutch') == 'Welkom'
    assert greet('IP_ADDRESS_INVALID') == 'Welcome'
    assert greet('czech') == 'Vitejte'
    assert greet('danish') == 'Velkomst'
    assert greet('estonian') == 'Tere tulemast'
    assert greet('finnish') == 'Tervetuloa'
    assert greet('flemish') == 'Welgekomen'
    assert greet('french') == 'Bienvenue'
    assert greet('german') == 'Willkommen'
    assert greet('irish') == 'Failte'
    print('Tests passed/')