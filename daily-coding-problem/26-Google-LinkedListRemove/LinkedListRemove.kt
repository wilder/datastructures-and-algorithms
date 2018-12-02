/**
 *
 * This problem was asked by Google.
 *
 * Given a singly linked list and an integer k, remove the kth last element from the list.
 * k is guaranteed to be smaller than the length of the list.
 * 
 * The list is very long, so making more than one pass is prohibitively expensive.
 * Do this in constant space and in one pass.
 */

import java.util.*

fun removeKthLast(linkedList: LinkedList<Int>, positionFromEnd: Int): LinkedList<Int> {
    val targetPosition = linkedList.size - positionFromEnd

    var index = 0
    val iterator = linkedList.iterator()
    for (element in iterator) {
        if (index == targetPosition) {
            iterator.remove()
            return linkedList
        }
        index++
    }

    return linkedList

}


fun main(args: Array<String>) {
    val linkedList1 = LinkedList<Int>(mutableListOf(1,2,3,4,5,6))
    assert(removeKthLast(linkedList1, 2).toIntArray().contentEquals(intArrayOf(1,2,3,4,6)))
    val linkedList2 = LinkedList<Int>(mutableListOf(1,2,3,4,5,6))
    assert(removeKthLast(linkedList2, 1).toIntArray().contentEquals(intArrayOf(1,2,3,4,5)))
    val linkedList3 = LinkedList<Int>(mutableListOf(1,2,3,4,5,6))
    assert(removeKthLast(linkedList3, 6).toIntArray().contentEquals(intArrayOf(2,3,4,5,6)))
}