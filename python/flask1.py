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

