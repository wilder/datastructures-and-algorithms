#!/bin/python3

import sys

def maximumPerimeterTriangle(l):
    final = (0, 0, 0)
    l.sort()
    current = 0
    lenght = len(l)
    while current + 2 < lenght:
        if l[current] + l[current +1] > l[current + 2]:
            curr_triangle = (l[current], l[current +1], l[current + 2])
            if sum(final) < sum(curr_triangle) :
                final = curr_triangle
            else:
                if final[0] < l[current]:
                    final = curr_triangle
        current += 1
    return final

if __name__ == "__main__":
    n = int(input().strip())
    l = list(map(int, input().strip().split(' ')))
    result = maximumPerimeterTriangle(l)
    if result != (0, 0, 0):
        print (" ".join(map(str, result)))
    else:
        print(-1)



