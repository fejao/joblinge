#!/usr/bin/env python

print("array_02")

###
### Write a Python program to append a new item to the end of the array.
###

arr_1 = [
    'a',
    'b',
    'c'
]

print("arr_1: %s" % arr_1 )
arr_1.append('d')
print("arr_1: %s" % arr_1 )
arr_1.insert(3,'dd')
print("arr_1: %s" % arr_1 )
arr_1.insert(2,'bb')
print("arr_1: %s" % arr_1 )

# arr_1.__len__()
# 6
