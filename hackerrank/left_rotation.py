#!/bin/python3

"""
https://www.hackerrank.com/challenges/array-left-rotation/problem
"""

import math
import os
import random
import re
import sys

from collections import deque

def left_rotate(queue, rotations_count):

    normalized_rotations_count = rotations_count % len(queue)

    index = 0
    while index < rotations_count:
        first = queue.popleft()
        queue.append(first)
        index += 1
    
    return queue


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = deque(map(int, input().rstrip().split()))

    print(" ".join(map(str, left_rotate(a, d))))
