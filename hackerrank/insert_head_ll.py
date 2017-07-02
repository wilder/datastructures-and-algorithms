def Insert(head, data):
    new_head = Node(data)
    new_head.next = head
    return new_head
