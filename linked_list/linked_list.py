from node import Node

class LinkdList(object):
    def __init__(self):
        self.head = None
    
    # Insert Node at the end 
    def Insert(self, data):
        if self.head == None:
            self.head = Node(data)
    
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = Node(data)
