def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump / mpg <= fuel_left


if __name__ == '__main__':
    assert zero_fuel(50, 25, 2) == True
    assert zero_fuel(100, 50, 1) == False
    print('Tests passed/')