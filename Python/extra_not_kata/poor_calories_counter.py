""" 
Lets say you want to stay fit but keep eating McDonalds… You have the brilliant idea to write a quick 
function that computes the number of calories in your McDonalds order. Well use the table below as our abridged McDonalds menu:

Item	Calories
Hamburger	250
Cheese Burger	300
Big Mac	540
McChicken	350
French Fries	230
Salad	15
Coca Cola	150
Sprite	150


You need to store this information in a python constant to create a kind of database. For this challenge we will declare our constant directly in the program.py file we are working with, instead of importing it.


For instance, below is an example of dict saved to a constant - AGE_OF_STUDENTS - that contains students and their ages:

AGE_OF_STUDENTS = {
  "Peter": 21,
  "George": 22,
  "Mary": 20
}
Dont forget to read the documentation about dicts. You will use them all the time, so make friends with them 😊

Specs
Create a poor_calories_counter function which takes three string arguments and returns the total number of calories for the three items of your order.

your function should make use of a Dictionary (obviously!)
your function must use our given calorie values! eg:
poor_calories_counter("McChicken", "French Fries", "Sprite")
#=> 730
your function should return “item_name not found” if an item is not in the dictionary eg:
poor_calories_counter("Big Mac", "Salad", "Shrimp Po Boy") 
#=> "Shrimp Po Boy not found" 
# """

def poor_calories_counter(*args):
    macdonals_db = {
        'Hamburger': 250,
        'Cheese Burger': 300,
        'Big Mac': 540,
        'McChicken': 350,
        'French Fries': 230,
        'Salad': 15,
        'Coca Cola': 150,
        'Sprite': 150
    }

    total_kcal = 0

    for item in args:
        try:
            total_kcal += macdonals_db[item]
        except KeyError:
            return f'{item} not found'

    return total_kcal
        
    

if __name__ == "__main__":
    assert poor_calories_counter("Hamburger", "Cheese Burger", "Big Mac") == 1090
    assert poor_calories_counter("Big Mac", "Salad", "Coca Cola") == 705
    assert poor_calories_counter("McChicken", "French Fries", "Sprite") == 730
    assert poor_calories_counter("Shrimp", "French Fries", "Salad") == 'Shrimp not found'
