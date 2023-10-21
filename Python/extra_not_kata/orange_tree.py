""" Let’s create an OrangeTree class which models the life of an orange tree (its birth, 
life cycle and death). Our class should incluce the following attributes: age, height, 
fruits, all integers, and dead a boolean.

To simulate time passing, you will need to implement the following instance method:

one_year_passes
pick_a_fruit
def one_year_passes(self):
  # TODO: age the tree by one year
  # TODO: check if the tree has survived
  # TODO: if so, make the tree height grow
  # TODO: if so, make the tree grow fruits
Specs
Each year, the tree should age by 1 year (it becomes older and taller, and eventually dies).
A tree grows 1 meter per year up to and including the 10th year. Then it stops growing
The orange tree cannot die until it reaches 50 years old.
After 50 years, the probability of dying increases each year Pyhon’s random library might come in handy 😉.
No tree can live more than 100 years.
A tree will produce 100 fruits a year once it is more than 5 years old.
A tree will produce 200 fruits a year when it reaches 10 years old.
A tree will not produce fruits once it reaches 15 years old.
You should be able to pick a single fruit from the tree by calling the pick_a_fruit method on 
your tree (but only if there are some left).
At the end of each year, the fruits which have not been picked will fall off. 
"""

import random

class OrangeTree:  
    def __init__(self):
        self.age = 0
        self.height = 0
        self.fruits = 0
        self.dead = False
    
    def one_year_passes(self):
        if not self.dead:
            self.age += 1
            
            # Tree growth logic
            if self.age <= 10:
                self.height += 1  # Grow 1 meter per year for the first 10 years

            # Fruit production logic
            if self.age > 5 and self.age < 10:
                self.fruits = 100
            elif self.age >= 10 and self.age < 15:
                self.fruits = 200
            else:
                self.fruits = 0  # No fruits after 15 years

            # Probability of dying logic
            if self.age >= 50:
                probability_of_dying = (self.age - 50) / 50
                if random.random() < probability_of_dying:
                    self.dead = True
                    print(f"The tree died at {self.age} years old.")
        
    def pick_a_fruit(self):
        if not self.dead and self.fruits > 0:
            self.fruits -= 1
            print("You picked a fruit!")
        elif not self.dead:
            print("There are no fruits left to pick.")
        else:
            print("The tree is dead, and you cannot pick fruits from it.")

if __name__ == "__main__":
    tree = OrangeTree()
    while tree.age < 100 and not tree.dead:
        tree.one_year_passes()

    


