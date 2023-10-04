"""
Now, let's say you want to improve your calorie counter, so that it can accept a list of
drinks, burgers, sides, and MEALS. Let's add these 3 meals to our menu:

Meal	Items in Meal
Happy Meal	Cheese Burger, French Fries, Coca Cola
Best Of Big Mac	Big Mac, French Fries, Coca Cola
Best Of McChicken	McChicken, Salad, Sprite


You may want to store these meals in another constant. Note: don't try to pre-compute the calories for each meal, 
just store the dishes that make up the meal. How do you think you could represent the dishes in each meal?

Let's now create an advanced_calories_counter function that will enable us to calculate calories of a combination of 
both our meals and our individual dishes

Specs
Our function should take a list of any size containing meals and individual dish items, eg:
orders = ["French Fries", "Happy Meal", "Sprite", "Best Of McChicken"]
advanced_calories_counter(orders)
#=> 1575
Our function should still return 'item_name not found' if the dish is not available
"""

def advanced_calories_counter(orders):

    macdonals_db = {
        'Hamburger': 250,
        'Cheese Burger': 300,
        'Big Mac': 540,
        'McChicken': 350,
        'French Fries': 230,
        'Salad': 15,
        'Coca Cola': 150,
        'Sprite': 150,
        'Happy Meal': ['Cheese Burger', 'French Fries', 'Coca Cola'],
        'Best Of Big Mac': ['Big Mac', 'French Fries', 'Coca Cola'],
        'Best Of McChicken': ['McChicken', 'Salad', 'Sprite']
    }
    
    total_kcal = 0
    
    for order in orders:
        try:
            if order in macdonals_db:
                if isinstance(macdonals_db[order], int):
                    total_kcal += macdonals_db[order]
                elif isinstance(macdonals_db[order], list):
                    sub_items = macdonals_db[order]
                    sub_total = advanced_calories_counter(sub_items)
                    if sub_total == 0:
                        return f'{order} not found'
                    total_kcal += sub_total
            else:
                return f'{order} not found'
        except KeyError:
            return f'{order} not found'

    return total_kcal

if __name__ == "__main__":
    
    assert advanced_calories_counter(['Happy Meal', 'Best Of Big Mac', 'Best Of Royal Cheese']) == 'Best Of Royal Cheese not found'
    assert advanced_calories_counter(["Big Mac", "French Fries", "Happy Meal", "Coca Cola"]) == 1600
    assert advanced_calories_counter(["Best Of Big Mac", "Salad", "Happy Meal", "Sprite"]) == 1765
    assert advanced_calories_counter(["Happy Meal", "McChicken"]) == 1030
    assert advanced_calories_counter(["Fish and Chips", "Salad"]) == 'Fish and Chips not found'
    print("All tests passed")
