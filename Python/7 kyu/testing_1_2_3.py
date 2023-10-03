""" 
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"] 
"""


def number(lines: list) -> list:
    return [f"{i+1}: {x}" for i, x in enumerate(lines)]


if __name__ == "__main__":
    assert number([]) == []
    assert number(["a", "b", "c"]) == ["1: a", "2: b", "3: c"]
    print("All tests passed")
