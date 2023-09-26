""" The function is given a balanced parentheses string. Each open "(" has corresponding closed ")". Compute the total score based on the following rules:

    Substring s = "()" has score 1, therefore, '()' should return 1

    Substring "s1s2" has total score as score of "s1" + score of "s2", therefore, '()()' should return 1+1 = 2

    Substring "(s)" has total score as 2 * score of "s", therefore '(())' should return 2*1 = 2

    Calculate the total score of the given expression and return it as integer.
 """
import unittest

def eval_parentheses(s: str) -> int:
    stack = []
    score = 0

    for char in s:
        if char == '(':
            stack.append(score)
            score = 0
        else:
            popped_score = stack.pop()
            score = popped_score + max(2 * score, 1)

        #print(f"my score is {score} and my stack has {stack}")
    
    #print("---Finish---")
    
    return score

class TestOrderWeight(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(eval_parentheses("()"), 1)
        self.assertEqual(eval_parentheses("(())"), 2)
        self.assertEqual(eval_parentheses("()()"), 2)
        self.assertEqual(eval_parentheses("((())())"), 6)
        self.assertEqual(eval_parentheses("(()(()))"), 6)
        self.assertEqual(eval_parentheses("()(())"), 3)
        self.assertEqual(eval_parentheses("()((()))"), 5)

if __name__ == "__main__":
    unittest.main()

