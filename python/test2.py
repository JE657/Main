# def lazy_range(up_to):
#     """Generator to return the sequence of integers from 0 to up_to, exclusive."""
#     index = 0
#     while index < up_to:
#         yield index
#         index += 1

# for i in lazy_range(20):
#     print(i)

# candies = [2, 3, 5, 1, 3]
# extraCandies = 3

# should_have = []
# greatest = False
# i = 0
# j = 0
# while 1:
#     print(f'{i} / {j}')
#     if candies[i] + extraCandies < candies[j]:
#         print(candies[i] + extraCandies)
#         should_have.append(False)
#     else:
#         should_have.append(True)
#         if j < len(candies) - 1:
#             j += 1
#         if i < len(candies) - 1:
#             i += 1
#         else:
#             break


# remaining_time = 20 * 60

# for i in range(20):
#     remaining_time *= 0.9
#     print(f'{i} seeds: {remaining_time}')

board = [11, 10, 9, 8, 7, 9, 10, 11,
         12, 12, 12, 12, 12, 12, 12, 12,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 1, 1, 1, 1, 1, 1,
         2, 3, 4, 5, 6, 4, 3, 2,
         ]


def changeTile(_col, _row, _val):
    board[_row * cols + _col] = _val


def getTile(_col, _row):
    return board[_row * cols + _col]


def flip(col, row):
    tmp = getTile(row, col)
    changeTile(row, col, getTile(row, 8 - 1 - col))
    changeTile(row, 8 - 1 - col, tmp)


cols = rows = 8

_x = 3
_y = 4

for i in range(_x - 1, _x + 2):
    for j in range(_y - 1, _y + 2):
        if(board.getTile)


# print(*board)

# for i in range(len(board)):

#     changeTile(i, 0, temp)


# # for i in range(cols):
# print(*board)
# # for j in range(rows):
# # changeTile(i, j)


# for j in range(len(board)):
#     print(board[j], end='')


# print("\n")
# flip(6, 3)

# for j in range(len(board)):
#     print(board[j], end='')
