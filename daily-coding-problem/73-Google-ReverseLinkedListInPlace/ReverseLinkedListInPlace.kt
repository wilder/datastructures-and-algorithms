/**
 *
 * Good morning! Here's your coding interview problem for today.
 *
 * This problem was asked by Google.
 *
 * Given the head of a singly linked list, reverse it in-place.
 */
import kotlin.test.assertEquals

data class Node<E> (val value: E, var next: Node<E>? = null) {
    fun toList(): List<E> {
        val values = mutableListOf<E>()
        var node: Node<E>? = this
        while (node != null) {
            values.add(node.value)
            node = node.next
        }
        return values
    }
}

fun <E> reverseLinkedList(head: Node<E>): Node<E> {
    var parent: Node<E>? = null
    var currentNode: Node<E>? = head

    while (currentNode != null) {
        val next = currentNode.next
        currentNode.next = parent
        parent = currentNode
        currentNode = next
    }

    return parent!!
}

fun main(args: Array<String>) {

    val node5 = Node(5)
    val node4 = Node(4, node5)
    val node3 = Node(3, node4)
    val node2 = Node(2, node3)
    val node1 = Node<Int>(1, node2)

    val reversedList = reverseLinkedList(node1)
    assertEquals(
        listOf(5, 4, 3, 2, 1),
        reversedList.toList()
    )

}
