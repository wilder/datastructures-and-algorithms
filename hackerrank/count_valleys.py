#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    
    valleys_count = 0
    level = 0
    
    for step in s:
        if step == 'U':
            level += 1
            if level == 0:
                valleys_count += 1
        if step == 'D':
            level -= 1
            
    return valleys_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

