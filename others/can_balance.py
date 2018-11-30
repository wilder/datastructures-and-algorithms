# -*- coding: utf-8 -*-
"""

Given a non-empty array, return true if there is a place to split the array 
so that the sum of the numbers on one side is equal to the sum of the numbers
on the other side.

canBalance([1, 1, 1, 2, 1]) → true
canBalance([2, 1, 1, 2, 1]) → false
canBalance([10, 10]) → true

----solutions----
solution 1
    #Summary: for each element, add to the leftsum
    for each of the next elements, add to the
    right sum. check if left and right match,
    if not, erase right sum and repeat
    #Time complexity: O(n^2)

solution 2
    #Summary: get the sum of the elements. 
    iterate the array, while iterating,
    subtract the current item from the sum
    and add it to subtracted. If subtracted (left)
    is equals to sum (right) return True
    #Time complexity: O(n)
"""

#solution 2
def can_balance(arr):
    
    elem_sum = sum(arr)
    subtracted = 0
    for elem in arr:
        elem_sum -= elem
        subtracted += elem

        if subtracted == elem_sum:
            return True

    return False

assert can_balance([1, 1, 1, 2, 1])
assert not can_balance([2, 1, 1, 2, 1])
assert can_balance([10, 10])
