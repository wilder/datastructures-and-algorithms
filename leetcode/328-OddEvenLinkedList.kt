/**
 * Odd Even Linked List
 * https://leetcode.com/problems/odd-even-linked-list/
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
    fun oddEvenList(head: ListNode?): ListNode? {
        
        val evenHead = head?.next
        var oddHeadAux = head
        var evenHeadAux = evenHead
        
        while (evenHeadAux?.next != null) {
            oddHeadAux?.next = evenHeadAux?.next
            evenHeadAux?.next = oddHeadAux?.next?.next
            oddHeadAux = oddHeadAux?.next //3
            evenHeadAux = evenHeadAux?.next //4
        }
        
        if (evenHeadAux?.next != null) {
            oddHeadAux?.next = evenHeadAux?.next
            oddHeadAux = oddHeadAux?.next
        }
        
        oddHeadAux?.next = evenHead
        return head
        
    }
}
