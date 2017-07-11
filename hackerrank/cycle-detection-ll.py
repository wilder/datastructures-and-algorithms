def has_cycle(head):
    if not head.next:
        return 0
    if head.next.next == head:
        return 1
    has_cycle(head.next)
    
