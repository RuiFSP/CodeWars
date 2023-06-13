from typing import List, Union


def unique_in_order(sequence: Union[str, List]) -> List:
    """
    Returns a list of items without any elements with the same value next to each other.

    :param sequence: A string or a list of items.
    :return: A list of items without consecutive duplicates.
    """
    if not sequence:
        return []

    if isinstance(sequence, str):
        sequence = list(sequence)

    result = [sequence[0]]
    for i in range(1, len(sequence)):
        # Check if the current element is different from the previous one
        if sequence[i] != sequence[i - 1]:
            result.append(sequence[i])
    return result


if __name__ == "__main__":
    assert unique_in_order("") == []
    assert unique_in_order([]) == []
    assert unique_in_order(()) == []
    assert unique_in_order("A") == ["A"]
    assert unique_in_order(["A"]) == ["A"]
    assert unique_in_order(("A",)) == ["A"]
    assert unique_in_order("AA") == ["A"]
    assert unique_in_order("AAAABBBCCDAABB") == ["A", "B", "C", "D", "A", "B"]
    assert unique_in_order("ABBCcAD") == ["A", "B", "C", "c", "A", "D"]
    assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]
    assert unique_in_order([1, 2, 3, 3, -1]) == [1, 2, 3, -1]
    print("All tests passed successfully")
