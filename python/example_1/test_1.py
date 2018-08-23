

def f1(var1, var2):
    return var1 + var2

def f2 (v1, v2):
    if v1 > v2:
        return v1
    else:
        return v2

def f3 (v1, v2):
    if len(v1) > len(v2):
        return v1
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
