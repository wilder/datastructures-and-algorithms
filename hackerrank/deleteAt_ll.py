def Delete(head, position):
    if position == 0:
        return head.next
    
    track_head = head
    for _ in range(position-1):
        head = head.next
    head.next = head.next.next 
    
    return track_head
