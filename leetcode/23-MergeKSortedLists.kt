/**
 * 
 * 23. Merge k Sorted Lists
 * https://leetcode.com/problems/merge-k-sorted-lists/
 *
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 * Solved using Count Sort approach
 */
import java.util.*
class Solution {
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        val grouppedNodes: Map<Int, List<ListNode>> = groupNodes(lists)
        return mergeLists(grouppedNodes)
    }
    
    fun groupNodes(lists: Array<ListNode?>): Map<Int, List<ListNode>> {
        val grouppedNodes = TreeMap<Int, MutableList<ListNode>>()
        lists.forEach { value ->
            var head = value
            while (head != null) {
                grouppedNodes.computeIfAbsent(head.`val`) { mutableListOf() }
                    .add(head)   
                head = head.next
            }
        }    
        return grouppedNodes
    }
    
    fun mergeLists(grouppedNodes: Map<Int, List<ListNode>>): ListNode? {
        var head: ListNode? = null
        var pastNode: ListNode? = null
        grouppedNodes.forEach { k, v ->
            v.forEach { node ->
                if (head == null) {
                    head = node
                    pastNode = node
                }
                pastNode?.next = node
                pastNode = node
            }
        }
        pastNode?.next = null
        return head
    }
}
