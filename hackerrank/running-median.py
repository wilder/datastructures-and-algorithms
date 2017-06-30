#!/bin/python

import sys

def find_median(arr):
    arr.sort()
    l_arr = len(arr)
    if l_arr & 1:
        return arr[l_arr/2]
    return sum(arr)/l_arr

n = int(raw_input())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = float(raw_input())
    a.append(a_t)
    print find_median(a)
