import random
import math

magic_const = 3

square = [[0 for i in range(magic_const)] for i in range(magic_const)]


def printsq():
    for row in square:
        print(row)


def setp(_x, _y, _v):
    square[wrap(_y)][wrap(_x)] = _v


def getp(_x, _y):
    return square[_x][_y]


def wrap(n):
    change = False
    if n == magic_const:
        n = 0
        change = True
    if n < 0:
        n += magic_const
        change = True

    return n

# rows = 3, cols = 3
x = y = math.ceil(magic_const / 2) - 1
print(x, y)
# printsq()

for i in range(magic_const * magic_const):
    num = i + 1
    filled = False

    if getp(wrap(x - 1), wrap(y + 1)) != 0:
        y -= 1

    else:
        x = wrap(x - 1)
        y = wrap(y + 1)

    setp(x, y, num)

    print([x, y], end='')

    print("")
    printsq()
