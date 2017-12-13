#!/bin/python
'''
q -> number of queries
n-cities m-#roads c-libcost c-roadcost
   {u v
mx {u v
   {u v
'''

from collections import defaultdict

def dfs(v, graph, visited):
    count = 1
    #print 'visiting '+str(v)
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            count+= dfs(i, graph, visited)
    return count

def main():

    q = int(raw_input())
    for _ in xrange(q):
        adjacency_dict = defaultdict(list)
        visited = {}

        n, m, clib, croad = map(int, raw_input().split())
    
        for _ in xrange(m):
            u, v = map(int, raw_input().split())
            #undirected graph
            adjacency_dict[u].append(v)
            adjacency_dict[v].append(u)
            visited[u], visited[v] = False, False
        
        repaired = 0 #number of repaired roads
        connected = 0

        for k, v in visited.iteritems():
            if not v: #k is not visited
                repaired += dfs(k, adjacency_dict, visited)-1
                connected+=1
        #print str(repaired)+'sss'
        if (croad > clib):
            final_cost = clib*n
            print final_cost
            continue
        else:
            final_cost = (connected*clib) + (repaired*croad)
        
        #alone cities
        final_cost += (n - len(visited)) * clib
            
        print final_cost

main()
    
