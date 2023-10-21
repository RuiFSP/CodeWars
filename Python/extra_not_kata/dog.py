""" 
Inheritance is a core concept of OO programming. It allows us to 
“transfer” methods by defining subclasses (children) that inherit 
from superclasses (parents). A child class will inherit from its parents' methods.

Specs
We have created a Dog class with one instance method: bark
Create a new class GermanShepherd which inherits the bark method from its parent class

For example, the code below should work:

german_shepherd = GermanShepherd()
german_shepherd.bark()    # => "woof woof" 
"""

class Dog:
    def bark(self):
        print("woof woof")
        
        
class GermanShepherd(Dog):
    pass