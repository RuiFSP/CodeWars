word_to_num = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
}


def parse_int(s):
    words = s.split()
    result = 0
    num = 0
    for word in words:
        if word == 'and':
            continue
        elif '-' in word:
            hyphen_parts = word.split('-')
            hyphen_sum = sum([word_to_num[part] for part in hyphen_parts])
            num += hyphen_sum
        elif word == 'hundred':
            num *= 100
        elif word == 'thousand':
            result += num * 1000
            num = 0
        elif word == 'million':
            result += num * 1000000
            num = 0
        else:
            num += word_to_num[word]
    result += num
    return result


if __name__ == "__main__":
    assert parse_int('one') == 1
    assert parse_int('twenty') == 20
    assert parse_int('two hundred forty-six') == 246
    assert parse_int('seven hundred eighty-three thousand nine hundred and nineteen') == 783919
    print('OK')
