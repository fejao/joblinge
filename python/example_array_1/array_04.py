#!/usr/bin/env python

print("array_04")

###
### Write a Python program to reverse the order of the items in the array
###

essen = [
    "ham",
    "eggs",
    "spam",
    "nuts"
]

def f1 (edibles):
    for food in edibles:
        if food == "spam":
            print("No more spam please!")
            break
        print("Great, delicious " + food)
    else:
        print("I am so glad: No spam!")

    print("Finally, I finished stuffing myself")
