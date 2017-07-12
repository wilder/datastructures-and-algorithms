def FindMergeNode(headA, headB):
    from collections import defaultdict
    x = defaultdict(int)
    
    while headA:
        x[headA.data] = x[headA.data] + 1
        headA = headA.next
    
    while headB:
        if x[headB.data] == 1:
            return headB.data
        headB = headB.next
    return None
