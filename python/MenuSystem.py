""" 

PROGRAM AUTHOR: Jordan Evan
FIND THIS SCRIPT @ MY REPOSITORY: HTTPS://GITHUB.COM/OMNIJK

PROGRAM NAME: MENU SYSTEM
PROGRAM DESCRIPTION:Utilize a basic menu loop to choose different calculation methods
                    based on user input.
                    
                    Originally Written for College and repurposed to be posted on GitHub.


"""

# Part 1: Bookstore

# Print name
print('Jordan-Lee Evan')

# Input original price from user
original_price = float(input('Enter the original price: '))
# Input markup and discount rates then divide by 100 to obtain a
# percentage form
markup_rate = (float(input('Enter the markup rate: ')) / 100) + 1
discount_rate = float(input('Enter the sale discount rate: ')) / 100

# Print bookstore header
print('*** ACME BOOKSTORE ***')

# Using "Cleaner" and slightly different style of formatting
print('Original Price = ${0:.2f}'.format(original_price), sep='')
print('Markup rate = {0:.2f}%'.format(markup_rate), sep='')
print('Discount rate = {0:.2f}%'.format(discount_rate), sep='')

# Print
print('Price after Markup = ${0:.2f}'.format(
    original_price * markup_rate), sep='')
print('Discount = ${0:.2f}'.format(original_price * discount_rate), sep='')
print('Please Pay: ${0:.2f}'.format(
    (original_price * markup_rate) - (original_price * discount_rate)), sep='')


# Part 2: BMI Calculator
# Formula taken from
# https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html
# Formula weight (lb) / height (in)^2 x 703
print('BMI Calculator')
weight_pounds = int(input('Enter your weight in pounds: '))
height_feet = int(input('Enter your height in feet: '))
height_inches = int(input('Enter your weight in inches: '))
bmi = 703 * (weight_pounds) / math.pow(((height_feet * 12) + height_inches), 2)
print('Your weight = {0} pounds'.format(weight_pounds))
print('Your height = {0} feet {1} inches'.format(height_feet, height_inches))
print('Your BMI = {0:.2f}'.format(bmi))
