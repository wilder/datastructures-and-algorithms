'''
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        # Extra field
        self.visited = False
    


"""
    Solution 1 - If the linkedlist data structure can be modified
    Use a visited property
    O(M + N) Time
    O(1) Space
"""

def findIntersection(l1, l2):
    
    node = l1
    while node:
        node.visited = True
        node = node.next

    node = l2
    while node:
        if node.visited:
            return node.value
        node = node.next

    return None

"""
    Solution 2 - Use a dict to keep track of the visited nodes
    O(M + N) time
    O(N) space
"""
def findIntersection2(l1, l2):
    
    visited = {}

    node = l1
    while node:
        visited[node.value] = True
        node = node.next

    node = l2
    while node:
        if node.value in visited:
            return node.value
        node = node.next

    return None


