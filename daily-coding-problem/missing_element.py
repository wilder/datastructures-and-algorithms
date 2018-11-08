'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''

#Time: O(n log n) and Space: O(1) solution
def missing_element(array):
    
    if not array:
        return None
    
    array.sort()
    last = array[0]
    for index in range(1, len(array)):
        current = array[index]
        if current > 0 and current - last > 1:
            return last + 1
        if current < 0:
            last = 0
        else:
            last = current
    
    return array[-1] + 1

assert missing_element([3,1,3,5,1,3,3,3,3,1,2,3,5,5,0,1,2,3,1,2]) == 4
assert missing_element([-1, -4, 3, 3, 2, 0, 2, 5]) == 1
assert missing_element([-1, -2, 3, 4, 1, 2]) == 5
assert missing_element([0]) == 1

        
