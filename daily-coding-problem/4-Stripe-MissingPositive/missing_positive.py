'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''

'''
O(n) time solution - O(n) space.
Create a hash table with the the key as the number and value a boolean.
For each of the numbers in the array, add it to the dict
For each of the elements in the array, check if element+1 is in the dict
if not, check if it is smallest than the last missing
return the smallest missing element
'''
import sys
def missing_element(array):
    index = dict([element, True] for element in array)
    lowest_missing = sys.maxint
    for element in array:
        if element < 0:
            continue
        if element + 1 not in index:
            if element + 1 < lowest_missing:
                lowest_missing = element + 1
    return lowest_missing
        
    


assert missing_element([3,1,3,5,1,3,3,3,3,1,2,3,5,5,0,1,2,3,1,2]) == 4
assert missing_element([-1, -4, 3, 3, 2, 0, 2, 5]) == 1
assert missing_element([-1, -2, 3, 4, 1, 2]) == 5
assert missing_element([0]) == 1

        
