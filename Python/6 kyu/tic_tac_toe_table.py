"""
Do you have in mind the good old TicTacToe?

Assuming that you get all the data in one array, you put a space around each
value, | as a columns separator and multiple - as rows separator, with something
like ["O", "X", " ", " ", "X", " ", "X", "O", " "] you should be returning this
structure (inclusive of new lines):

 O | X |
-----------
   | X |
-----------
 X | O |

Now, to spice up things a bit, we are going to expand our board well beyond a
trivial 3 x 3 square and we will accept rectangles of big sizes, still all as a
long linear array.

For example, for "O", "X", " ", " ", "X", " ", "X", "O", " ", "O"] (same as
above, just one extra "O") and knowing that the length of each row is 5, you
will be returning

 O | X |   |   | X
-------------------
   | X | O |   | O

And worry not about missing elements, as the array/list/vector length is always
going to be a multiple of the width.
 """

def display_board(board:list, width:int) -> str:
    row_strings = []
    for i in range(0, len(board), width):
        row = board[i:i + width]
        print(row)
        row_str = " | ".join(row)
        print(row_str)
        row_strings.append(f" {row_str} ")

        if i < len(board) - width:  # Check if it's not the last row
            row_strings.append("-" * (len(row_strings[0])))

    return '\n'.join(row_strings)

if __name__ == "__main__":
    assert(display_board(["O", "X", "X", "O"],2) == " O | X \n-------\n X | O ")
    assert(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " "],3) == " O | X |   \n-----------\n   | X |   \n-----------\n X | O |   ")
    assert(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " ", "O"],5) == " O | X |   |   | X \n-------------------\n   | X | O |   | O ")
    assert(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " ", "O"],2) == " O | X \n-------\n   |   \n-------\n X |   \n-------\n X | O \n-------\n   | O ")
    assert(display_board(["1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1"],6) == " 1 | 2 | 3 | 4 | 5 | 1 \n-----------------------\n 2 | 3 | 4 | 5 | 1 | 2 \n-----------------------\n 3 | 4 | 5 | 1 | 2 | 3 \n-----------------------\n 4 | 5 | 1 | 2 | 3 | 4 \n-----------------------\n 5 | 1 | 2 | 3 | 4 | 5 \n-----------------------\n 1 | 2 | 3 | 4 | 5 | 1 ")
