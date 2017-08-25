# -*- coding: utf-8 -*-
'''
Consider the leftmost and righmost appearances of some value in an array. We'll say that the "span" is the number of elements between the two inclusive. A single value has a span of 1. Returns the largest span found in the given array.

maxSpan([1, 2, 1, 1, 3]) → 4
maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6

------------------------------------

#solution 1
  summary: for each element i in the array, iterate from 
           the next position to the last (j). Update the
           last position where j == i. if the difference
           of the position of the elements i and j is
           bigger than the biggest difference, it is the biggest.
           Return the biggest.
  time complexity: O(n^2)

#solution 2
  summary: make a dict of {value:[positions]}. 
           Iterate over the list. For each item,
           add to the dict the item:index.

           iterate over the dict. Get the biggest difference between
           the last and fist position of the current list.
  time complexity: O(n)
  


'''

#solution 2

from collections import defaultdict 

def get_max(val_pos_dict):
    biggest_span = 0
    for _, v in val_pos_dict.iteritems():
        span = v[-1]+1 - v[0]
        if span > biggest_span:
            biggest_span = span
    return biggest_span

def solution(arr):
    
    #dict of value and its positions
    val_pos = defaultdict(list)

    #mapping values
    for i, v in enumerate(arr):
        val_pos[v].append(i)

    
    return get_max(val_pos)

print solution([1, 2, 1, 1, 3])
print solution([1, 4, 2, 1, 4, 1, 4])
print solution([1, 4, 2, 1, 4, 4, 4])
