#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def is_filled(position):
    return position == 1

def is_in_bound(grid, i, j):
    return (i >= 0 and i < len(grid)) and (j >= 0 and j < len(grid[0]))

def is_in_bound_and_filled(grid, i, j):
    return is_in_bound(grid, i, j) and is_filled(grid[i][j])

def map_adjacents(grid):
    adjacents = defaultdict(list)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #print("is filled {0}: {1}".format((i, j), is_filled(grid[i][j])))
            if is_filled(grid[i][j]):
                left = i - 1
                if is_in_bound_and_filled(grid, left, j):
                    adjacents[(i,j)].append((left, j))
                right = i + 1
                if is_in_bound_and_filled(grid, right, j):
                    adjacents[(i,j)].append((right, j))
                up = j - 1
                if is_in_bound_and_filled(grid, i, up):
                    adjacents[(i,j)].append((i, up))
                down = j + 1
                if is_in_bound_and_filled(grid, i, down):
                    adjacents[(i,j)].append((i, down))
                up_left = (i-1, j-1)
                if is_in_bound_and_filled(grid, up_left[0], up_left[1]):
                    adjacents[(i,j)].append(up_left)
                up_right = (i-1, j+1)
                if is_in_bound_and_filled(grid, up_right[0], up_right[1]):
                    adjacents[(i,j)].append(up_right)
                bottom_left = (i+1, j-1)
                if is_in_bound_and_filled(grid, bottom_left[0], bottom_left[1]):
                    adjacents[(i,j)].append(bottom_left)
                bottom_right = (i+1, j+1)
                if is_in_bound_and_filled(grid, bottom_right[0], bottom_right[1]):
                    adjacents[(i,j)].append(bottom_right)
    return adjacents

def dfs(position, grid, adjacents_map):
    print("visiting {}".format(position))
    counter = 1
    # marks as visited
    grid[position[0]][position[1]] = -1
    for child in adjacents_map[position]:
        if grid[child[0]][child[1]] != -1: # if not visited
            counter += dfs(child, grid, adjacents_map)
    return counter
 
def maxRegion(grid):
    adjacents_map = map_adjacents(grid)
    max_region = 1
    
    for position in adjacents_map:
        if grid[position[0]][position[1]] != -1: # not visited
            region_count = dfs(position, grid, adjacents_map)
            if region_count > max_region:
                max_region = region_count
    return max_region

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()

