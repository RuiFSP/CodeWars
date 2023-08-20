import math


def get_participants(handshakes: int) -> int:
    """
    Returns the number of participants in a party given the number of handshakes.
    """
    if handshakes == 0:
        return 0
    farmers = (math.sqrt(8 * handshakes + 1) + 1) / 2
    # The number of farmers must be a whole number, so we round up.
    return math.ceil(farmers)


if __name__ == "__main__":
    assert get_participants(0) == 0
    assert get_participants(1) == 2
    assert get_participants(3) == 3
    assert get_participants(6) == 4
    assert get_participants(7) == 5
    print("All tests passed.")
