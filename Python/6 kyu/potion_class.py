""" 
This is your first potion class in Hogwarts and professor gave you a homework to figure out what 
color potion will turn into if he'll mix it with some other potion. All potions have some color that 
written down as RGB color from [0, 0, 0] to [255, 255, 255]. To make task more complicated teacher will 
do few mixing and after will ask you for final color. Besides color you also need to figure out what volume 
will have potion after final mix.

Task
Based on your programming background you managed to figure that after mixing two potions colors will mix as 
if mix two RGB colors. For example, if you'll mix potion that have color [255, 255, 0] and volume 10 with one 
that have color [0, 254, 0] and volume 5, you'll get new potion with color [170, 255, 0] and volume 15. So you 
decided to create a class Potion that will have two properties: color (a list (a tuple in Python) with 3 integers) 
and volume (a number), and one method mix that will accept another Potion and return a mixed Potion.

Example
felix_felicis       =  Potion([255, 255, 255],  7)
shrinking_solution  =  Potion([ 51, 102,  51], 12)
new_potion          =  felix_felicis.mix(shrinking_solution)

new_potion.color   ==  [127, 159, 127]
new_potion.volume  ==  19
Note: Use ceiling when calculating the resulting potion's color. 
"""

import math

class Potion:
    def __init__(self, color: tuple, volume:int) -> None:
        self.color = color
        self.volume = volume
    
    def mix(self, other:object) -> object:
        new_potion_volume = self.volume + other.volume
        
        new_potion_color = []
        
        for i in range(len(self.color)):
            weighted_sum = math.ceil((self.color[i] * self.volume + other.color[i] * other.volume) / new_potion_volume)
            new_potion_color.append(weighted_sum)

        
        return Potion(tuple(new_potion_color),new_potion_volume)        
        

def basic_tests():
    potions = [
        Potion((153, 210, 199), 32),
        Potion((135,  34,   0), 17),
        Potion((18,   19,  20), 25),
        Potion((174, 211,  13),  4),
        Potion((255,  23, 148), 19),
        Potion((51,  102,  51),  6)
    ]
    
    a = potions[0].mix(potions[1])
    b = potions[0].mix(potions[2]).mix(potions[4])
    c = potions[1].mix(potions[2]).mix(potions[3]).mix(potions[5])
    d = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[4]).mix(potions[5])
    e = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[3]).mix(potions[4]).mix(potions[5])
    
    assert a.color == (147, 149, 130)
    assert a.volume == 49
    assert b.color == (135, 101, 128)
    assert b.volume == 76
    assert c.color == (74, 50, 18)
    assert c.volume == 52
    assert d.color == (130, 91, 102)
    assert d.volume == 99
    assert e.color == (132, 96, 99)
    assert e.volume == 103
    
    print("All tests passed")
    
if __name__ == "__main__":
    basic_tests()