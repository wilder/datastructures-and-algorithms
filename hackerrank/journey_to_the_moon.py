'''
The member states of the UN are planning to send  people to the Moon. But there is a problem. In line with their principles of global unity, they want to pair astronauts of  different countries.

There are  trained astronauts numbered from  to . But those in charge of the mission did not receive information about the citizenship of each astronaut. The only information they have is that some particular pairs of astronauts belong to the same country.

Your task is to compute in how many ways they can pick a pair of astronauts belonging to different countries. Assume that you are provided enough pairs to let you identify the groups of astronauts even though you might not know their country directly. For instance, if  are astronauts from the same country; it is sufficient to mention that  and  are pairs of astronauts from the same country without providing information about a third pair . 

Input Format

The first line contains two integers,  and , separated by a single space.  lines follow. Each line contains integers separated by a single space  and  such that


and  and  are astronauts from the same country.

Constraints

Output Format

An integer that denotes the number of permissible ways to choose a pair of astronauts.

https://www.hackerrank.com/challenges/journey-to-the-moon/problem

Time Complexity: O(|v+e|)
Space Complexity: O(n) 
'''

#!/bin/python3
from collections import defaultdict
import sys

def dfs(v, adjacents, visited):
    counter = 1
    visited[v] = True
    for child in adjacents[v]:
        if not visited[child]:
            counter += dfs(child, adjacents, visited)
    return counter

if __name__ == "__main__":
    sys.setrecursionlimit(sys.getrecursionlimit())
    n, p = map(int, input().strip().split())
    possibilities = 0
    paired = 0
    adjacents = defaultdict(list)
    visited = defaultdict(lambda: False)

    for _ in range(p):
        p1, p2 = map(int, input().split())
        adjacents[p1].append(p2)
        adjacents[p2].append(p1)

    for i in range(n):
        v = visited[i]
        if not v:
            group_len = dfs(i, adjacents, visited)
            possibilities += paired * group_len
            paired += group_len
    print(possibilities)
    

