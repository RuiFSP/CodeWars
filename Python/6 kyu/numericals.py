from typing import Dict


def numericals(s: str) -> str:
    """
    Replaces each symbol in the string with the occurrence count.

    Args:
        input_string: The input string to process.

    Returns:
        The modified string with symbols replaced by occurrence count.
    """
    symbol_count: Dict[str, int] = {}
    output_string = ""

    for symbol in s:
        if symbol not in symbol_count:
            symbol_count[symbol] = 1
        else:
            symbol_count[symbol] += 1

        output_string += str(symbol_count[symbol])

    return output_string


if __name__ == "__main__":
    assert numericals("Hello, World!") == "1112111121311"
    assert numericals("Hello, World! It's me, JomoPipi!") == "11121111213112111131224132411122"
    assert numericals("hello hello") == "11121122342"
    assert numericals("aaaaaaaaaaaa") == "123456789101112"
    print("All tests passed successfully!")
