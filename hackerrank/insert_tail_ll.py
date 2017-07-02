def Insert(head, data):
    if head == None:
        return Node(data)
    
    last_node = head
    while last_node.next != None:
        last_node = last_node.next
    last_node.next = Node(data)
    return head
