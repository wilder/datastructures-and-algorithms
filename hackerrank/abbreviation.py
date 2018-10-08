#!/bin/python3

import math
import os
import random
import re
import sys

# aDaBCd - ABC

def capitalize_next_lower(string):
    capitalized = None
    for i in range(len(string)):
        if string[i].islower():
            capitalized = string[:i] + string[i].upper() + string[i+1:]
    return capitalized

def delete_next_lower(string):
    capitalized = None
    for i in range(len(string)):
        if string[i].islower():
            capitalized = string[:i] + string[i+1:]
    return capitalized

# Complete the abbreviation function below.
def abbreviation(a, b):

    if a == b:
        return True

    if len(a) < len(b):
        return False

    capitalized = capitalize_next_lower(a)

    if capitalized == None:
        # there is no more lowercase letters
        return False

    return abbreviation(capitalized, b) or abbreviation(delete_next_lower(a), b)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        if result:
            fptr.write('YES\n')
        else:
            fptr.write('NO\n')

    fptr.close()
