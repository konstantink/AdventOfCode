#!/usr/bin/python3

def calculate_fuel(mass, fuel = 0):
    added_fuel = int(mass / 3) -2
    if (added_fuel <= 0):
        return fuel
    
    fuel += added_fuel
    return calculate_fuel(added_fuel, fuel)

def calc():
    total_fuel = 0
    with open('/Users/user/Downloads/day1-puzzle1-input.txt', 'rb') as f:
        for input_mass in f.readlines():
            total_fuel += calculate_fuel(int(input_mass))
            print("Input {} output {}".format(input_mass, calculate_fuel(int(input_mass))))

    print("Total fuel: {}".format(total_fuel))
