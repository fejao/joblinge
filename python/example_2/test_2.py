#!/usr/bin/env python

from test_1 import f1

def f2(v):
    return f1(v) + 1

print("%d" % f2(5))
