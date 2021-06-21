# %matplotlib inline
# from matplotlib import pyplot as plt
import numpy as np

# each point is length, width, type (0, 1)
data = [[3,   1.5, 1],
        [2,   1,   0],
        [4,   1.5, 1],
        [3,   1,   0],
        [3.5, .5,  1],
        [2,   .5,  0],
        [5.5,  1,  1],
        [1,    1,  0]]

mystery_flower = [4.5, 1]

# activation function


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# derivative of activation function


def sigmoid_p(x):
    return sigmoid(x) * (1 - sigmoid(x))


def relu(x):
    return max(0.01, x)


def train():
    # random init of weights
    w1 = np.random.randn()
    w2 = np.random.randn()
    b = np.random.randn()
    iterations = 10000
    learning_rate = 0.1

    for i in range(iterations):
        # get a random point
        ri = np.random.randint(len(data))
        point = data[ri]
        z = point[0] * w1 + point[1] * w2 + b

        # networks prediction
        pred = relu(z)
        target = point[2]

        # cost for current random point
        cost = np.square(pred - target)

        # start differentiate to apply for chain rule
        # differentiate cost respect to pred
        dcost_dpred = 2 * (pred - target)

        # differentiate pred respect to z
        dpred_dz = relu(z)

        # differentiate z respect to w1
        dz_dw1 = point[0]

        # differentiate z respect to w2
        dz_dw2 = point[1]

        # differentiate z respect to b
        dz_db = 1

        # apply chain rule
        dcost_dz = dcost_dpred * dpred_dz
        dcost_dw1 = dcost_dz * dz_dw1
        dcost_dw2 = dcost_dz * dz_dw2
        dcost_db = dcost_dz * dz_db

        w1 = w1 - learning_rate * dcost_dw1
        w2 = w2 - learning_rate * dcost_dw2
        b = b - learning_rate * dcost_db

    return w1, w2, b

w1, w2, b = train()

# predict what the myster flower is!
z = w1 * mystery_flower[0] + w2 * mystery_flower[1] + b

pred = relu(z)

print(pred)

# print(“close to 0 -> blue, close to 1 -> red”)
