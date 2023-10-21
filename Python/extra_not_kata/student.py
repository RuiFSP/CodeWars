""" 
Suppose you have students (defined by the class Student) who each have an 
amount of money (in bills of five, ten and twenty euro). We want to be able to 
compare them based on their wealth. Let's create a class Student which will store 
all their information and help with comparing

Specs
When initializing a Student, you should require 4 additional arguments, the student's
name and the number of bills they own (fives, tens and twenties)
Implement a wealth method on Student. When called it should return the total wealth of the student
Implement a compare method which takes one argument, another student, and returns the name of 
the richer student
Optional
Implement an advanced_compare method which takes one argument, a list of students. When called, 
it should return a list of all the student's names sorted from most wealthy to least wealthy….
don't forget to include the student instance the method was called on in the sort 😉

Hint - This stackoverflow post might help 
"""

class Student:
    
    def __init__(self,name,num_fives,num_tens,num_tweenties):
        self.name = name
        self.num_fives = num_fives
        self.num_tens = num_tens
        self.num_tweenties = num_tweenties
        
    def wealth(self):
        return self.num_fives * 5 + self.num_tens * 10 + self.num_tweenties * 20
    
    def compare(self,other_student):
        return self.name if self.wealth() > other_student.wealth() else other_student.name
    
    def advanced_compared(self,list_of_students):
        
        # Calculate the wealth of each student in the list
        wealth_list = [(student, student.wealth()) for student in list_of_students]
        print(wealth_list)
        
        # Sort the list based on wealth in descending order
        sorted_wealth_list = sorted(wealth_list, key=lambda x: x[1], reverse=True)
        
        # Extract the names of the students in the sorted list
        sorted_names = [student.name for student, _ in sorted_wealth_list]
        
        return sorted_names
    
    def __repr__(self):
        return f"Student('{self.name}', {self.num_fives}, {self.num_tens}, {self.num_tweenties})"  
    

if __name__ == "__main__":
    one = Student('Amy', 5, 6, 7)
    two = Student('Bilbo', 3, 4, 5)
    three = Student('Chuck', 2, 3, 4)
    four = Student('Diane', 1, 2, 3)
    

    print(one.wealth())
    print(two.wealth())
    print(three.wealth())
    print(four.wealth())
    
    print(one.compare(two))
    
    print(one.advanced_compared([one,two,three,four]))