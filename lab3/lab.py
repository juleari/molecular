# -*- coding: utf-8 -*-
from random import randint
import string

TAIL = ["CH3"]
BODY = ["NH", "O", "CH2"]
HEAD = ["SO4Na", "COOK", "COONa", "OH"]

LEN_BODY = len(BODY) - 1
LEN_HEAD = len(HEAD) - 1

N = {
    "CH3"   : -0.5,
    "CH2"   : -0.5,
    "O"     : 1.3,
    "OH"    : 1.9,
    "NH"    : 9.4,
    "COONa" : 19.1,
    "COOK"  : 21.1,
    "SO4Na" : 38.7
}

INITF = [
    ["CH3"] + 10 * ["CH2"] + ["O"] + 2 * ["CH2"] + ["SO4Na"],
    ["CH3"] + 16 * ["CH2"] + ["COOK"],
    ["CH3"] + 11 * ["CH2"] + ["OH"]
]

def G(f): return sum([ N[m] for m in f]) + 7

def mutation(f):

    b = randint(1, 2)

    if b == 2: i = randint(1, len(f) - 2)

    return  f[:-1] + [ HEAD[randint(0, LEN_HEAD)] ] if b == 1 else \
            f[: i] + [ BODY[randint(0, LEN_BODY)] ] + f[i + 1:]

def replace(f0, i, l, f1):
    return f0[ : i] + f1 + f0[ i+l: ]

def transfer(f0, f1):

    # 1: all in body
    # 2: body and head
    # 3: only head
    b = randint(1, 3)

    lf= [len(f0), len(f1)]
    m = [l - 2 for l in lf]
    
    l = [randint(1, m[0]), randint(1, m[1])] if b < 3 else (1, 1)
    t = [lf[0] - l[0] - 1, lf[1] - l[1] - 1]
    i = [randint(1, t[0]), randint(1, t[1])] if b == 1 else \
        [ t[0], t[1] ]                       if b == 2 else \
        [ m[0], m[1] ]

    return [replace(f0, i[0], l[0], f1[i[1] : i[1]+l[1]]), 
            replace(f1, i[1], l[1], f0[i[0] : i[0]+l[0]])]

def iteration(f):

    mut = mutation(f)
    return addnew([mut] + transfer(mut, f))

def addnew(a):

    f = []
    for i in a: 
        if i not in f: f.append(i)

    return f

def generation(farr):

    while len(farr) < 100:
        l = len(farr)
        for j in range(l): 
            farr.extend([i for i in iteration(farr[j]) if i not in farr])

    return farr

def printf(f): print "%s: %s\n" % (string.join(f, "-"), G(f))

def main(): [printf(f) for f in generation(INITF) if G(f) <= 13 and G(f) >= 8]

main()