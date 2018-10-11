#!/usr/bin/env python

def f1(v1):
    for i in range(0, v1):
        print("i = %d" % i)

def f1_1(v1):
    for zahler in range(0, v1):
        print("zahler = %d" % zahler)

# def f2(5):
#     for i in range(1, (5 + 1)):
#         print("i = %d" % i)
# >>> f2(5)
# i = 1
# i = 2
# i = 3
# i = 4
# i = 5

def f2(v1):
    for i in range(1, (v1 + 1)):
        print("i = %d" % i)

def f3(var):
    zahler = 0
    while(zahler < var):
        print("zahler = %d" % zahler)
        zahler = zahler + 1

def f5(var):
    zahler = 1
    while(zahler <= var):
        print("zahler = %d" % zahler)
        zahler = zahler + 1

f1(5)
print("---------")
f2(5)
print("---------")
f3(5)
print("---------")
f5(5)
