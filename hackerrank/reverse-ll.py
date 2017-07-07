def Reverse(head):
    if not head:
        return
    
    nodes = []
    while head.next:
        nodes.append(head.data)
        head = head.next
    nodes.append(head.data)
    
    head = Node(nodes[-1])
    auxhead = head
    for i in reversed(nodes[:-1]):
        auxhead.next = Node(i)
        auxhead = auxhead.next
    
    return head
        
