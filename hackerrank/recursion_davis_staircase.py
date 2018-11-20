#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-recursive-staircase

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

