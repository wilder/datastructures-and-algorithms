#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    result = 0
    socks_dict = defaultdict(lambda: 0)
    for i in ar:
        socks_dict[i] += 1
        
    for _, v in socks_dict.items():
        result += int(v/2)
    
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

