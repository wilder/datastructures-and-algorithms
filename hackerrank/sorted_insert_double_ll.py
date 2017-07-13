def SortedInsert(head, data):
    if not head:
        return Node(data)
    if head.data >= data:
        #link it to the left
        head.prev = Node(data)
        head.prev.next = head
        return head.prev
    else:
        #goes until the last biggest value and return its head
        front = SortedInsert(head.next, data)
        #link this new front to the next
        head.next = front
        front.prev = head
    return head
            
