/**
 *
 * Binary Tree Zigzag Level Order Traversal
 * https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
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
import java.util.*
class Solution {
    fun zigzagLevelOrder(root: TreeNode?): List<List<Int>> {
        
        if (root == null) {
            return emptyList()
        }
        
        val result = mutableListOf(listOf<Int>(root!!.`val`))
        
        val queue = LinkedList<TreeNode>()
        queue.addAll(getChildren(root, false))
        
        var reversed = true
        
        while(!queue.isEmpty()) {
            val next = mutableListOf<TreeNode>()
            val visited = mutableListOf<Int>()
            while(!queue.isEmpty()){
                val current = queue.removeLast()
                visited.add(current.`val`)
                next.addAll(getChildren(current, reversed))
            }
            result.add(visited.toList())
            queue.addAll(next)
            reversed = !reversed
        }
    
        return result
        
    }
    
    fun getChildren(node: TreeNode, reversed: Boolean): List<TreeNode> {
        if (node.left == null && node.right == null) {
            return emptyList()
        }
        
        if (node.left == null) {
            return listOf(node.right)
        }
        
        if (node.right == null) {
            return listOf(node.left)
        }
        
        if (reversed) {
            return listOf(node.right, node.left)
        }
        
        return listOf(node.left, node.right)
    }
}
