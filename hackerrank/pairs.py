#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    seen = {}
    pairs_count = 0
    for element in arr:
        if (element + k in seen):
            pairs_count += 1
        if (element - k in seen):
            pairs_count += 1
        seen[element] = True
    
    return pairs_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

