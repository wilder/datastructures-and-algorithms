def RemoveDuplicates(head):
    track_head = head
    while head.next:
        if head.data == head.next.data:
            head.next = head.next.next
        else:
            head = head.next
    return track_head
