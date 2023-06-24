from typing import List


def permutations(input_string: str) -> List[str]:
    """
    Generates all permutations of a non-empty input string and removes duplicates.

    Args:
        input_string: The input string.

    Returns:
        A list of permutations without duplicates.
    """
    permutations_list: List[str] = []

    def generate_permutations(n: int, string_list: List[str]) -> None:
        """
        Generates permutations recursively.

        Args:
            n: The length of the current substring.
            string_list: The list representation of the current substring.

        Returns:
            None
        """
        if n == 1:
            permutations_list.append("".join(string_list))
        else:
            for i in range(n):
                generate_permutations(n - 1, string_list)
                if n % 2 == 0:
                    string_list[i], string_list[n - 1] = string_list[n - 1], string_list[i]
                else:
                    string_list[0], string_list[n - 1] = string_list[n - 1], string_list[0]

    generate_permutations(len(input_string), list(input_string))
    return sorted(list(set(permutations_list)))


# alternative using itertools
# from itertools import permutations
# return list(set("".join(p) for p in permutations(input_string)))

if __name__ == "__main__":
    print("\n--- test permutations 1 ---")
    assert permutations("a") == ["a"]
    print("\n--- test permutations 2 ---")
    assert permutations("ab") == ["ab", "ba"]
    print("\n--- test permutations 3 ---")
    assert permutations("abc") == ["abc", "acb", "bac", "bca", "cab", "cba"]
    print("\nAll tests passed")
