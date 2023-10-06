""" 
So why do we need inheritance? Because we don't want to have the same logic repeated in multiple 
places in our code! If multiple classes share some of the same behaviour then it may be time to introduce inheritance.

e.g. You want to code a generic Parser with the basic features (read a file, store its content, etc.). After a while, 
you decide you want to create more specific parsers like XmlParser or a JsonParser to handle specific formats. By making 
these new classes children of the Parser class, it means you don't have to re-write all the basic methods created in Parser, 
and you only need to create the methods that are specific to your Xml or Json needs. So inheritance keeps things DRY!

Specs
Complete the class Dessert:

create instance variables for name and calories
create an instance method healthy which returns a bool. A dessert instance with fewer than 200 calories would be considered healthy
create an instance method delicious which returns a bool. All dessert instances should return True
Create the class JellyBean:

JellyBean should be a child of the Dessert class
JellyBean should take three arugments - name, calories, flavor
Keep your init method DRY with super()
JellyBean's delicious method should return the default set in the parent class, unless its flavor is black licorice, 
which is not delicious 
"""

class Dessert:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def healthy(self):
        return self.calories < 200

    def delicious(self):
        return True
	
class JellyBean(Dessert):
    def __init__(self, name, calories, flavor):
       super().__init__(name,calories)
       self.flavor = flavor
       
    def delicious(self):
        if self.flavor == 'black licorice':
            return not super().delicious()
        return super().delicious()
        
        
if __name__ == "__main__":
    print('\nTesting your Dessert methods\n')
    healthy_des = Dessert('cupcake', 100)
    unhealthy_des = Dessert('cake', 300)
    
    assert healthy_des.healthy() == True
    assert unhealthy_des.healthy() == False
    assert healthy_des.delicious() == True
    assert unhealthy_des.delicious() == True
    
    print("All Desert tests passed 😃\n")
    
    print('Testing your JellyBean methods\n')
    delicious_des = JellyBean('yummy', 100, 'cherry')
    gross_des = JellyBean('disgusting', 300, 'black licorice')
    
    assert delicious_des.healthy() == True
    assert gross_des.healthy() == False
    assert delicious_des.delicious() == True
    assert gross_des.delicious() == False
    
    print("All JellyBean tests passed 😃\n")