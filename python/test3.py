# import matplotlib.pyplot as plt

# fig = plt.figure()

# Base_Damage = 15
# Max_Charge = 50
# Total_Damage = 0


# nums = []

# for Current_Charge in range(0, 51):
#     Total_Damage = Base_Damage * 1.087 - 0.08 / \
#         (Current_Charge / Max_Charge + 0.07)
#     nums.append(Total_Damage)


# print(nums)

# _di = {}

# for i in range(29):
#     if i == 0:
#         _di.update({i: 1})
#     if i == 1:
#         _di.update({i: 0.65})
#     if i == 2:
#         _di.update({i: 0.86})
#     elif i >= 3 and i < 5:
#         _di.update({i: 0})
#     else:
#         _di.update({i: 0.92})


# sum1 = 0
# for i in _di:
#     sum1 += _di[i]

# print(sum1 / len(_di))

import random
import numpy as np
import math

# increase velocity of every object -2 down per second
gravity_vector = (0, -2, 0)
# So, before every update, we can modify our velocity:
velocity += gravity_vector * delta
# apply gravity effect
position += velocity * delta
# update position

# Let's just say our air is thick. So thick it slows down
# cannon balls by half every second.
velocity += gravity_vector * delta
# apply gravity effect
velocity *= 0.5 * delta
# apply 0.5 slowdown per second
position += velocity * delta


# print("Remainder ",  % 20)

# crit = 1.04
# dmg = 1.04

# base = 100

# sum_crit = 0
# sum_dmg = 0

# for i in range(100):
#     if random.uniform(0, 100 / crit) < 4:
#         sum_crit += base * crit
#     else:
#         sum_crit += base

#     sum_dmg += base * dmg


# print("Crit: %s Damage: %s" % (sum_crit, sum_dmg))
