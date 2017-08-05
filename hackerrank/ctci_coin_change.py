#!/bin/python
import sys

def is_valid(coin, value):
    return value - coin >= 0

def make_change(coins, n, solutions, ssolutions):
    if n <= 0:
        a = sorted(solutions)
        ssolutions.add(tuple(a))
        #print solutions

    for c in coins:
        if not is_valid(c, n):
            #adding value
            continue
        solutions.append(c)
        n-= c
        make_change(coins, n, solutions, ssolutions)
        n+=c
        if solutions:
            solutions.pop()


    
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
solution = set([])
make_change(coins, n, [], solution)
print len(solution)
