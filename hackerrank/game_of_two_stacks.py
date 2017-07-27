#!/bin/python

import sys

def play(a, b, x):
    s = 0
    removed = 0   
    while True:
        if s + a[-1] > x and s + b[-1] > x:
            return removed
        if (not a) and (not b):
            return removed
        if not a:
            if b[-1] + s > x:
                return removed
            s+= b.pop()
        elif not b:
            if a[-1] + s > x:
                return removed
            s+= b.pop()
        else:
            if a[-1] >= b[-1]:
                s+=b.pop()
            else:
                s+=a.pop()
        removed+=1 
        
            
g = int(raw_input().strip())
for a0 in xrange(g):
    n,m,x = raw_input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))

    print play(a[::-1], b[::-1], x)
