try:
    words
except:
    words = set( [ x.strip() for x in open('words','r').readlines() ] )

from itertools import *

while True:
    print
    print 

    while True:
        letters = raw_input( "Letters     >>> " )
        if len(letters)==12:
            break

    while True:
        x = raw_input("Num Letters >>> " )
        try:
            numLetters = int(x)
            break
        except:
            pass

    ret = []
    for x in permutations(letters, numLetters):
        s = "".join(x)
        if s in words:
            ret.append(s)

    chunks = 8
    while ret:
        print " ".join(ret[:chunks] )
        ret = ret[chunks:]

