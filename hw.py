def verify(p):
    return (True in [True for c in p if c.isupper()]) and (True in [True for c in p  if c.islower()]) and (True in [True for c in p if c.isdigit()])

#test verify(p)
print verify("a")
print verify("B")
print verify("12")
print verify("aBCd#$2")

def strength(p):
    if verify(p): #automatic fail
        print "fail verify"
        return 0
    if len(p) < 8:
        print "fail length"
        return 0
    print "made it this far"
    points =  1
    if len(p) > 12:
        points = points + 1
        print "len"
    upper= sum([1 if c.isupper() else 0 for c in p])
    if upper != 0:
        points = points + 2
        print "upper"
    lower = sum([1 if c.islower() else 0 for c in p])
    if lower != 0:
        points=points+ 2
        print "lower"
    dig = sum([1 if c.isdigit() else 0 for c in p])
    if dig != 0:
        points = points + 2
        print "dig"
    otherChars= ".?!&#,;:-_*"
    other = sum([1 if c in otherChars else 0 for c in p])
    if other != 0:
        points = points + 2
        print "other"
    return points
print strength("a")
print strength("abw3!oy;")
print strength("abwCC3!oy;")
