# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return 'Website content goes here.'

# if __name__ == '__main__':
#     app.run(debug=True)


# import random

# xp_needed = 118000

# con = 0
# medal_xp = 300

# seconds = 5 * 60
# current_xp = 0

# win_rate = 80

# for i in range(40):

#     current_xp += medal_xp + con + (seconds * 3.4)
#     if (random.randrange(1, 5) < 4):
#         current_xp += 500
#     con += 200
#     print("Games: {0} XP: {1}".format(i, current_xp))

# rudeCounter = 3

# HP = 3500

# kris_hit = 65
# susie_hit = 85
# r_hit = 50

# turn = 1

# while HP >= 0:
#     print("Turn Number: %s HP: %s" % (turn, HP))
#     HP -= kris_hit
#     HP -= r_hit
#     rudeCounter -= 1
#     if rudeCounter <= 0:
#         rudeCounter = 3
#         print("Rude Hit!")
#         HP -= 185
#     else:
#         HP -= susie_hit

#     turn += 1

# print("Dead on Turn: %s" % turn)

# Math module used for Squaring (math.pow() function) for BMI calculation
import math
# Name: Jordan-Lee Evan
# Course: IS115
# Date: 3/24/2021

# Description: Two small programs,
# one to calculate markups/discount rates
# one to calculate BMI (Body Mass Index)

# Questions 1-5:
# 1:
# 2:
# 3:
# 4:
# 5:
# Python Version: 3.7.7
# TK Version: 8.6.9
# IDLE Version: 3.7.7


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
