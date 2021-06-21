"""
    PROGRAM AUTHOR: Jordan Evan
    FIND THIS SCRIPT @ MY REPOSITORY: HTTPS://GITHUB.COM/OMNIJK

    PROGRAM DESCRIPTION: 
                        Assignment: "Write Python code that exercise your
                        understanding of functions and lists in Python."
                        
    
"""

# Note: Trying to be more conventional with my code with this one
import math  # Used for math.round


# Function to display header information
def display_header():
    print('Name: Jordan Evan\n'
          'Course Number: IS115-3001\n'
          'Time to complete assignment: 30 Minutes\n')


# Function for converting weight in pounds to kilograms
def pounds_to_kilograms(_pounds):
    return _pounds / 2.2


# Function for Calculating BMI using weight and height
def calculate_bmi(_pounds, _height_feet, _height_inches):
    return _pounds * 703 / math.pow(((_height_feet * 12) + _height_inches), 2)


def print_range(_start, _end, _step=1):
    if _start > _end:
        print('Error. Starting Value is greater than end value')
        return

    # for i in range(min(_start,_end), max(_start,_end), _step):
    for i in range(_start, _end+1, _step):
        print(i)


''' BEGIN MAIN FUNCTION '''


def main():
    display_header()
    weight_in_pounds = int(input('Enter a weight in pounds: '))
    while weight_in_pounds < 1:
        print('Invalid weight in pounds entered.')
        weight_in_pounds = int(input('Enter a weight in pounds: '))

    # Display pounds to kgs conversion using function
    print('Converted pounds to kilograms: {:.2f}'.format(pounds_to_kilograms(weight_in_pounds)))





    # Input height in feet and inches from user
    # Loop to validate for positive values
    height_in_feet = int(input('Enter your height in feet: '))
    while height_in_feet < 0:
        height_in_feet = int(input('Enter your height in feet: '))
    height_in_inches = int(input('Enter your height in inches: '))
    while height_in_inches < 0:
        height_in_inches = int(input('Enter your height in inches: '))

    print('Calculated BMI: {:.2f}'.format(calculate_bmi(weight_in_pounds,
                                                        height_in_feet,
                                                        height_in_inches)))

    start_input = int(input('Enter starting value of a set of numbers: '))
    end_input = int(input('Enter ending value of a set of numbers: '))
    increment_input = int(input('Enter the increment for the set of numbers: '))

    print_range(start_input, end_input, increment_input)


main()
''' END MAIN FUNCTION '''
