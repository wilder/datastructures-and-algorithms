#!/bin/python3

import math
import os
import random
import re
import sys

def bsearch(collection, target, start_pos, end_pos): #fix: use start and end position
    middle_pos = int((start_pos+end_pos)/2)
    
    if collection[-1] < target:
        return collection
    
    if start_pos == end_pos:
        return None
    
    middle_element = collection[middle_pos]
    
    if middle_element == target: #ok
        print("middle_element == target")
        print("middle_pos: "+str(middle_pos))
        return collection[:middle_pos+1]
    
    if middle_element > target: #ok
        return bsearch(collection, target, start_pos, middle_pos)
    
    if middle_element < target and middle_pos + 1 < len(collection) and collection[middle_pos + 1] > target: #ok
        print("third")
        return collection[:middle_pos+1]
    
    else:
        print("else")
        return bsearch(collection, target, middle_pos+1, end_pos)
    
def conbinations(a_elements, b_elements):
    return len(a_elements)*len(b_elements)

def triplets(a, b, c):
    triplets_count = 0
    for element in b:
        print('------' + str(element))
        a_elements = bsearch(a, element, 0, len(a))
        print(a_elements)
        if a_elements:
            c_elements = bsearch(c, element, 0, len(c))
            print(c_elements)
            if c_elements:
                triplets_count += conbinations(a_elements, c_elements)
    return triplets_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    print("------")
    print(arra, arrb, arrc)
    print("------")
    ans = triplets(sorted(arra), sorted(set(arrb)), sorted(arrc))

    fptr.write(str(ans) + '\n')

    fptr.close()

