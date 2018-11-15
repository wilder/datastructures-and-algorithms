'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 1, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''
from collections import defaultdict

def maxSubsetSum(array):

    if not array:
        return 0

    memo = defaultdict(lambda: 0)

    memo[0] = array[0]

    for i in range(1, len(array)):
        memo[i] = max(memo[i-2], max(memo[i-1], memo[i-2] + array[i]))

    return max(memo[len(array)-1], memo[len(array)-2])
