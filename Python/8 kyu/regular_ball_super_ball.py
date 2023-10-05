""" 
Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super" 
"""

class Ball:
    def __init__(self,ball_type="regular"):
        self.ball_type = ball_type
        

def basic_tests():
    assert Ball().ball_type == "regular"
    assert Ball("super").ball_type == "super"
    print("All tests passed")
    

if __name__ == "__main__":
    basic_tests()