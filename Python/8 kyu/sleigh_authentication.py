""" 
Christmas is coming and many people dreamed of having a ride with Santa's sleigh. 
But, of course, only Santa himself is allowed to use this wonderful transportation. 
And in order to make sure, that only he can board the sleigh, there's an authentication mechanism.

Your task is to implement the authenticate() method of the sleigh, which takes the 
name of the person, who wants to board the sleigh and a secret password. If, and only if, 
the name equals "Santa Claus" and the password is "Ho Ho Ho!" (yes, even Santa has a secret
password with uppercase and lowercase letters and special characters :D), the return value 
must be true. Otherwise it should return false.

Examples:

sleigh = Sleigh()
sleigh.authenticate('Santa Claus', 'Ho Ho Ho!') # must return True

sleigh.authenticate('Santa', 'Ho Ho Ho!') # must return False
sleigh.authenticate('Santa Claus', 'Ho Ho!') # must return False
sleigh.authenticate('jhoffner', 'CodeWars') # Nope, even Jake is not allowed to use the sleigh ;) 
"""


class Sleigh():
    
    def __init__(self,name="",password=""):
        self.name = name
        self.password = password
    
    def authenticate(self, name, password):
        return name == 'Santa Claus' and password == "Ho Ho Ho!"
    
def basic_tests():
    
    names = ['Santa Claus','Santa','Santa Claus','jhoffner']
    passwords = ['Ho Ho Ho!','Ho Ho Ho!','Ho Ho!','CodeWars']
    results = [True,False,False,False]
    
    for i in range(4):
        name,password,result=names[i],passwords[i],results[i]
        sleigh = Sleigh()
        assert sleigh.authenticate(name,password) == result
    
    print("All tests passed")
    
if __name__ == "__main__":
   basic_tests() 
    