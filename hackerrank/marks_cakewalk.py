#!/bin/python3

import sys

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    eaten = 0
    calories = 0
    for c in calorie:
        calories += pow(2, eaten) * c
        eaten += 1
    return calories
    
if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().strip().split(' ')))
    result = marcsCakewalk(calorie)
    print(result)
