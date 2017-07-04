from node import Node

class LinkdList(object):
    def __init__(self):
        self.head = None
    
    # Insert Node at the end 
    def insert_end(self, data):
        if self.head == None:
            self.head = Node(data)
    
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = Node(data)

    # Insert Node at the begining of the linked List
    def insert_beg(self, data):
        new_head = node(data)
        new_head.next = self.head
        self.head = new_head
    
    # Insert a node at a specific position
    def insertAt(self, data, position):
        if not self.head:
            self.head = Node(data)

        if position == 0:
            insert_beg(data)

        # getting the node that is before the desired position
        tmp_node = self.head
        for i in range(position - 1):
            tmp_node = tmp_node.next

        # node currently at the desired position
        aux_node = tmp_node.next
        tmp_node.next = Node(data, aux_node)

    # Deletes the node at the given position
    def Delete(self, position):
        if position == 0:
            self.head = self.head.next
    
        aux = self.head
        for _ in range(position-1):
            aux = aux.next
        aux.next = aux.next.next 
