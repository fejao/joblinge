#!/usr/bin/env python

def f1(var1, var2):
    return var1 + var2

def f2 (v1, v2):
    if v1 > v2:
        return v1
    else:
        return v2

def f2_2 (v1, v2):
    if v1 > v2:
        return v1
    elif v1 == v2:
        return ("%d ist gleich %d" % (v1, v2))
    else:
        return v2

def f3 (v1, v2):
    if len(v1) > len(v2):
        return v1
    else:
        return v2

def f3_2 (v1, v2):
    if len(v1) > len(v2):
        return v1
    elif len(v1) == len(v2):
        return ("len(%s) ist gleich len(%s)" % (v1, v2))
    else:
        return v2

def f4 (v1, v2):
    if v1 >= v2:
        # print("%f ist grosser als %f" % (v1,v2))
        print("%d ist grosser als %d" % (v1,v2))
    else:
        # print("%f ist grosser als %f" % (v2,v1))
        print("%d ist grosser als %d" % (v2,v1))

def f5 (v1, v2):
    if v1 == v2:
        print("%d ist gleich als %d" % (v1,v2))
    else:
        if v1 > v2:
            print("%d ist grosser als %d" % (v1,v2))
        else:
            print("%d ist grosser als %d" % (v2,v1))

def f99(v1, v2):
    if v1 == v2:
        print "GLEICH"
    else:
        print "NICHT GLEICH"

def f19(v1, v2):
    if v1 == v2:
        print "GLEICH"
    else:
        print "NICHT GLEICH"

# print (f3(2,3))
print (f3("aa bb","bb aa"))
print (f3("bb","aa"))
