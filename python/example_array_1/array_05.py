#!/usr/bin/env python

from math import sqrt

print("array_04")

###
###
###

essen = [
    "ham",
    "eggs",
    "spam",
    "nuts"
]

# def f1 (edibles):
#     for food in edibles:
#         if food == "spam":
#             print("No more spam please!")
#             break
#         print("Great, delicious " + food)
#     else:
#         print("I am so glad: No spam!")
#
#     print("Finally, I finished stuffing myself")

nummers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
]

# 1/2 = 0.5 x
# 2/2 = 1 :)
# 3/2 = 1.5 x
# 4/2 = 2 :)

def f1 (array):
    for i in array:
        if (i % 2 == 0):
            print("gefunden ins array: %d" % i)

def f2 (array):
    for i in array:
        if (i % 2 != 0):
            print("gefunden ins array: %d" % i)

def f3 (array):
    for i in array:
        if i > 3:
            break
        if (i % 2 == 0):
            print("gefunden ins array: %d" % i)

def f4():
    n = int(input("Maximal Number? "))
    for a in range(1,n+1):
        for b in range(a,n):
            c_square = a**2 + b**2
            c = int(sqrt(c_square))
            if ((c_square - c**2) == 0):
                print(a, b, c)

f1(nummers)
print('-----------')
f2(nummers)
print('-----------')
f3(nummers)
print('-----------')
f4()
