def ReversePrint(head):
    if not head:
        return
    
    nodes = []
    while head.next:
        nodes.append(head.data)
        head = head.next
    nodes.append(head.data)
    
    for i in reversed(nodes):
        print i
