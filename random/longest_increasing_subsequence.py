#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the longestIncreasingSubsequence function below.
def buildFromLink(sequence, subsequences_link, max_subsequence_index):
    subsequence = []
    i = max_subsequence_index
    while i != -1:
        subsequence.append(sequence[i])
        i = subsequences_link[i]

    return subsequence

def longestIncreasingSubsequence(sequence):

    subsequeces_length_at_position = [1 for i in sequence]
    subsequences_link = [-1 for i in sequence]

    for i in range(len(sequence)):
        max_index = -1
        max_length = -1
        for j in range(0, i):
            if sequence[j] < sequence[i]:
                subsequence_length = subsequeces_length_at_position[j] + subsequeces_length_at_position[i]
                if subsequence_length >= max_length:
                    max_length = subsequence_length
                    max_index = j

        if max_index != -1:
            subsequeces_length_at_position[i] = max_length
            subsequences_link[i] = max_index

    #print(sequence)
    #print(subsequences_link)
    return buildFromLink(sequence, subsequences_link, subsequeces_length_at_position.index(max(subsequeces_length_at_position)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = len(longestIncreasingSubsequence(arr))

    fptr.write(str(result) + '\n')

    fptr.close()
