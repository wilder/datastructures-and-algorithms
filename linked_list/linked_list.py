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
        new_head = node(data):
        new_head.next = self.head
        self.head = new_head
