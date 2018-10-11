#!/usr/bin/env python

print("array_01")

###
### 1. Write a Python program to create an array of 5 integers and display the array items.
### Access individual element through indexes.
###

arr_1 = []
arr_2 = []

# print("%s", dir(arr_1))
for i in range(0,5):
    arr_1.insert(i, i + 1)

for i in range(1,6):
    arr_2.insert(i, i)


kunde_arr = [
    'aaa',
    'bbb',
    23,
    'ccc'
]

kunde_dir = {
    'vorname': 'aaa',
    'nachname': 'bbb',
    'alt': 23,
    'addr': 'ccc'
    }

def f1 (arr, dir):
    i = 0
    for key, value in dir.items():
        if arr[i] == value:
            print("key: %s with value: %s ist der gleiche von %s" % (key, value, arr[i]))
        else:
            print("--> key: %s with value: %s ist der gleiche von %s" % (key, value, arr[i]))

        i = i + 1

# f1(kunde_arr, kunde_dir)
