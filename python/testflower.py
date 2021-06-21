import numpy as np

# sigmoid function


def nonlin(x, deriv=False):
    if(deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


def rel(x):
    return max(0.01, x)


# input dataset
X = np.array([[1, 1.5, 3],
              [0, 1, 2],
              [1, 1.5, 4],
              [0, 1, 3],
              [1, 0.5, 3.5],
              [0, 0.5, 2],
              [1, 1, 5.5],
              [0, 1, 1]])

# output dataset
# y = np.array([[1, 0, 1, 0, 1, 0, 1, 0]]).T
y = np.array([[4.5, 1]])

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((3, 1)) - 1

for i in range(10000):

    # forward propagation
    l0 = X
    l1 = rel(np.dot(l0, syn0)[0])

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * rel(l1)

    # update weights
    syn0 += np.dot(l0.T, l1_delta)

print(l1)
