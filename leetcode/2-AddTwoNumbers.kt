/**
 * Linked List - Add two numbers
 * https://leetcode.com/problems/add-two-numbers/
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        return addTwoNumbers(l1, l2, 0)
    }
    
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?, extra: Int): ListNode? {
        
        if (l1 == null && l2 == null) {
            if (extra != 0) {
                return ListNode(extra)
            }
            return null
        }
        
        var extra = extra
        var value1 = getValue(l1)
        var value2 = getValue(l2)
        var sum = value1 + value2 + extra
        extra = 0
        
        if (sum >= 10) {
            sum = sum - 10 
            extra = 1
        }
    
        val currentNode = ListNode(sum)
        currentNode.next = addTwoNumbers(l1?.next, l2?.next, extra)
        
        return currentNode
        
    }
    
    fun getValue(node: ListNode?): Int {
        if (node == null) {
            return 0
        }
        return node.`val`
    }
}
