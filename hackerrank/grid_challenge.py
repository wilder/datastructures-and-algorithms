#!/bin/python3

import sys

def gridChallenge(grid):
    # sort lines
    row_sorted_grid = []
    for row in grid:
        row_sorted_grid.append(sorted(row))
    
    #check if letters from the lines are ordered
    for row, _ in enumerate(row_sorted_grid):
        for column, _ in enumerate(row_sorted_grid[row]):
            #if it is not out of the grid bounds
            if row+1 < len(row_sorted_grid): 
                # if the current letter comes after the letter below
                if row_sorted_grid[row][column] > row_sorted_grid[row+1][column]: 
                    return 'NO'
    
    return 'YES'

if __name__ == "__main__":
    tn = int(input().strip())
    for t in range(tn):
        n = int(input().strip())
        grid = []
        grid_i = 0
        for grid_i in range(n):
            grid_t = str(input().strip())
            grid.append(grid_t)
        result = gridChallenge(grid)
        print(result)

