/**
 *
 * This problem was asked by Google.
 *
 * A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
 * Given the root to a binary tree, count the number of unival subtrees.
 *
 * For example, the following tree has 5 unival subtrees:
 *
 *       0 n1
 *      / \
 *     1   0 n2 n3
 *    / \
 *   1   0 n4 n5
 *  / \
 * 1     n6 n7
 *
 */

class Node(val value: Int, var parent: Node?, var left: Node?, var right: Node?)

fun countUnivalTrees(root: Node?): Int {

    if (root == null) return 0
    if (root.left == null && root.right == null) return 1

    val leftUnivalCount = countUnivalTrees(root.left)
    val rightUnivalCount = countUnivalTrees(root.right)

    var univalCount = leftUnivalCount + rightUnivalCount
    if((root.left == null || root.left!!.value == root.value) &&
        (root.right == null || root.right!!.value == root.value)) {
        univalCount += 1
    }

    return univalCount
}

fun main(args: Array<String>) {

    val root = Node(0, null, null, null)
    val node2 = Node(1, root, null, null)
    val node3 = Node(0, null, null, null)
    val node4 = Node(1, node2, null, null)
    val node5 = Node(0, node2, null, null)
    val node6 = Node(1, node4, null, null)
    val node7 = Node(1, node4, null, null)

    root.left = node2
    root.right = node3
    node3.parent = root
    node2.left = node4
    node2.right = node5
    node4.right = node6
    node4.left = node7

    assert(countUnivalTrees(root) == 5)

}
