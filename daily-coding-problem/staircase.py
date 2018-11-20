#!/bin/python3

'''
Daily Coding Problem: Problem #12

This Problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

import math
import os
import random
import re
import sys

steps = [1, 2, 3]

def backtrack(target, currentStep, memo):

    if currentStep in memo:
        return memo[currentStep]
    
    if currentStep > target:
        return 0
    
    if currentStep == target:
        return 1

    nWays = 0
    for s in steps:
        result = backtrack(target, currentStep+s, memo)
        memo[currentStep+s] = result
        nWays += result
    
    return nWays

def stepPerms(n):
    return backtrack(n, 0, {})

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()

