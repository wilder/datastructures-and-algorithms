def ReversePrint(head):
    if not head:
        return
    ReversePrint(head.next)
    print head.data
