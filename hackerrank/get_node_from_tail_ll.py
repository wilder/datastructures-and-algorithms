def GetNode(head, position):
    i = 0
    behind_node = head
    while head.next:
        '''the "behind_node" will only move after the head is "position" times ahead of it
            so it will end up at the given position counting backwards from the tail
        '''
        if i >= position:
            behind_node = behind_node.next
        head = head.next
        i+=1
    return behind_node.data
