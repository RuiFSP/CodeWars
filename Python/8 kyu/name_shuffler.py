def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


if __name__ == '__main__':
    assert name_shuffler('john McClane') == 'McClane john'
    assert name_shuffler('Mary jeggins') == 'jeggins Mary'
    assert name_shuffler('joseph johnson') == 'johnson joseph'
    print('Tests passed/')
