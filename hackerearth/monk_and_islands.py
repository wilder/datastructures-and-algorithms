'''
# Read input from stdin and provide input before running code

name = raw_input()
print 'Hi, %s.' % name
'''
from collections import defaultdict

test_cases = int(raw_input())

for _ in range(test_cases):
    final_island, m = map(int, raw_input().split())
    
    #reading bridges info
    adjacency_dict = defaultdict(list)
    for _ in range(m):
        i1, i2 =  map(int, raw_input().split())
        adjacency_dict[i1].append(i2)
        adjacency_dict[i2].append(i1)
    
    distance_dict = defaultdict(lambda: 0)
    current_distance = 1

    adjacents = [final_island]
    while adjacents:
        nexxt = []
        for island in adjacents:
            for v in adjacency_dict[island]:
                if(distance_dict[v] == 0):
                    distance_dict[v] = current_distance
                    nexxt.append(v)
        current_distance += 1
        adjacents = nexxt
    
    print distance_dict[1]
