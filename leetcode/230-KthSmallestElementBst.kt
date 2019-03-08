/**
 * https://leetcode.com/problems/kth-smallest-element-in-a-bst/
 * 230. Kth Smallest Element in a BST
 *
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {

    val smallest = mutableMapOf<Int, Int>()
    var order = 0

    fun kthSmallest(root: TreeNode?, k: Int): Int {
        mapSmallestOrder(root)
        print(smallest)
        return smallest[k]!!
    }

    fun mapSmallestOrder(root: TreeNode?) {
        if (root == null) {
            return
        }

        mapSmallestOrder(root.left)
        order++

        this.smallest[order] = root.`val`

        mapSmallestOrder(root.right)
    }

}
