"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
 
 debug
 NULL <-- 6 <--> 4 <--> 2 --> NULL
 
 aux = 4 <-> (2) <-> NULL
 next_node = 6 <--> (4) <--> 2
 aux = NULL <-> (2) <-> 4 
 
 aux = 6 <--> (4) <--> 2
 next_node = NULL <-- (6) <--> 4
 aux =  2 <-> (4) <-> 6
 
 aux = NULL <-- (6) <--> 4
 next_node = NULL
 aux = 2 4 6 null
 
"""
def Reverse(head):
    if not head:
        return head
    
    #moves head to the last
    while head.next:
        head = head.next
    
    #keeps the head being the last node
    aux = head
    
    #reverse next with prev until the begin of the list
    while aux:
        next_node = aux.prev
        aux.next, aux.prev = aux.prev, aux.next
        aux = next_node
    
    #erasing old prev
    head.prev = None
    return head
