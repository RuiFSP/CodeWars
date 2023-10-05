""" 
self is an important concept to understand when working with classes. By using the 
self keyword we can access the attributes and methods of the class in python. It helps 
us to represent the instance of the class that is passing through our methods.

Here we have an incorreclty constructed Cat class with three different methods which are 
being used to update an instance’s attributes:

age_10_years
gain_weight
turn_grey
Specs
Get the winning combination

Update the Cat class by placing the self keyword where needed
No new methods are needed
The class is correct when you run the file and see the following print out in the terminal:
"My 1 year old cat weighs 5 pounds and is brown.  Come back in a few years and see how he is doing"
--------------------10 years later----------------------
"My 10 year old cat now weighs 20 pounds and is grey "
Hint - notice that the instance methods are being chained in line 22 🤔, chaining will be an 
important part of our machine learning pipelines in the future. This article on method chaining may help. 
"""

class Cat:
    def __init__(self):
        self.age = 1
        self.color = 'brown'
        self.weight = 5

    def age_10_years(self):
        self.age = 10
        return self

    def gain_weight(self):
        self.weight = 20
        return self

    def turn_grey(self):
        self.color = 'grey'
        return self


# Do not modify the code below:
cat = Cat()
print(f"My {cat.age} year old cat weighs {cat.weight} pounds and is {cat.color}.  Come back in a few years and see how he is doing.")


cat.age_10_years().gain_weight().turn_grey()
print("--------------------10 years later----------------------")
print(f"My {cat.age} year old cat now weighs {cat.weight} pounds and is {cat.color}")