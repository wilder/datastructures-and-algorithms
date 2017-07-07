def CompareLists(headA, headB):
    
    while headA and headB:
        if headA.data != headB.data:
            return 0
        headA = headA.next
        headB = headB.next
    
    if (headA and not headB) or (headB and not headA):
        return 0
    
    return 1
  
