/**
 * 
 * 86. Partition List
 * https://leetcode.com/problems/partition-list/submissions/
 *
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    
    fun partition(head: ListNode?, x: Int): ListNode? {
        
        var head = head
        var leftHead: ListNode? = null
        var leftTail: ListNode? = null
        var rightHead: ListNode? = null
        var rightTail: ListNode? = null
        
        while (head != null) {
            if (head.`val` < x) {
                if (leftHead == null) {
                    leftHead = head
                } else {
                    leftTail?.next = head!!
                }
                leftTail = head
            } else {
                if (rightHead == null) {
                    rightHead = head
                } else {
                    rightTail?.next = head
                }
                rightTail = head
            }
            head = head.next
        }
        
        if (leftTail == null) {
            return rightHead
        }
        
        merge(leftTail, rightHead, rightTail)
        return leftHead
    }
    
    fun merge(leftTail: ListNode?, rightHead: ListNode?, rightTail: ListNode?) {
        leftTail?.next = rightHead
        rightTail?.next = null
    }
    
}
