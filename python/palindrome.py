import math
import random

n = 1200

n1 = 797
n2 = 313

# n1 = 1
# n2 = 500


def reverse(n):
    orig = n
    new = 0
    zeroCounter = 0
    while orig > 0:
        remainder = orig % 10
        new10 = new * 10
        if(remainder != 0):
            new = new10 + remainder
        else:
            zeroCounter += 1

        orig //= 10
        print(remainder, new10, " / ", orig, new)

    for i in range(zeroCounter):
        new *= 10

    return new

print(reverse(n))


def is_prime(n):
    i = 2
    while(i * i <= n):
        if(n % i == 0):
            return False
        i += 1

    return True


def is_palin(n):
    return (reverse(n) == n)


primes = []
palins = []
print(n1, n2)
is_palin(n)

# for j in range(min(n1, n2), max(n1, n2) + 1, 1):
#     if(is_prime(j) and is_palin(j)):
#         # primes.append(j)
#         print(j, "", end='')

# for p in primes:
#     if(is_palin(p)):
#         palins.append(p)

# print(palins)
# print(palin(n))

# num = 15
# mode = 3
# print(num % mode)
# print(num // mode)
