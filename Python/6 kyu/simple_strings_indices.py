"""
In this Kata, you will be given a string with brackets and an index of an
opening bracket and your task will be to return the index of the matching
closing bracket. Both the input and returned index are 0-based except in
Fortran where it is 1-based. An opening brace will always have a closing brace.
Return -1 if there is no answer
(in Haskell, return Nothing; in Fortran, return 0; in Go, return an error)
Examples

solve("((1)23(45))(aB)", 0) = 10 -- the opening brace at index 0 matches the closing brace at index 10
solve("((1)23(45))(aB)", 1) = 3
solve("((1)23(45))(aB)", 2) = -1 -- there is no opening bracket at index 2, so return -1
solve("((1)23(45))(aB)", 6) = 9
solve("((1)23(45))(aB)", 11) = 14
solve("((>)|?(*'))(yZ)", 11) = 14

Input will consist of letters, numbers and special characters, but no spaces. The only brackets will be ( and ).

More examples in the test cases.

Good luck!
"""

def solve(st:str, idx:int) -> int:
    if st[idx] != '(':
        return -1  # The character at idx is not an opening parenthesis

    stack = []
    for i in range(idx, len(st)):
        if st[i] == '(':
            stack.append(st[i])
        elif st[i] == ')':
            stack.pop()
            if not stack:
                return i

    return -1  # No matching closing parenthesis found



if __name__ == "__main__":
    assert solve("((1)23(45))(aB)",0) == 10
    assert solve("((1)23(45))(aB)",1) == 3
    assert solve("((1)23(45))(aB)",2) == -1
    assert solve("((1)23(45))(aB)",6) == 9
    assert solve("((1)23(45))(aB)",11) == 14
    assert solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",11) == 28
    assert solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",0) == 29
    assert solve("(>_(va)`?(h)C(as)(x(hD)P|(fg)))",19) == 22
