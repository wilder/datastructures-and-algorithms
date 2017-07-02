def InsertNth(head, data, position):
    if head == None:
        return Node(data)
    
    if position == 0:
        new_head = Node(data)
        new_head.next = head
        return new_head
    
    #getting the node that is before the desired position
    tmp_node = head
    for i in range(position - 1):
        tmp_node = tmp_node.next
 
    #node currently at the desired position
    aux_node = tmp_node.next   
    tmp_node.next = Node(data, aux_node)
    return head
