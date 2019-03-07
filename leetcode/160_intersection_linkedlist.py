#
# Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        listA_size = self.countNodes(headA)
        listB_size = self.countNodes(headB)

        difference = abs(listA_size - listB_size)

        if listA_size > listB_size:
            headA = self.getHeadAfterDifference(headA, difference)

        else:
            headB = self.getHeadAfterDifference(headB, difference)

        return self.getIntersection(headA, headB)


    def countNodes(self, head):
        count = 0

        while(head != None):
            head = head.next
            count += 1

        return count

    def getHeadAfterDifference(self, biggestHead, difference):
        index = 0
        while index != difference:
            biggestHead = biggestHead.next
            index += 1
        return biggestHead


    def getIntersection(self, headA, headB):
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
