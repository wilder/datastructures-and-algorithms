/**
 * 
 * Iterative Binary Tree Inorder Traversal
 * https://leetcode.com/problems/binary-tree-inorder-  traversal/submissions/
 * 
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
    fun inorderTraversal(root: TreeNode?): List<Int> {
        
        if (root == null){
            return emptyList()
        }
        
        val resultList = mutableListOf<Int>()
        val stack = LinkedList<TreeNode>()
        stack.push(root!!)
        
        while(stack.peek().left != null) {
            stack.push(stack.peek().left)
        }
        
        while(stack.peek() != null) {
            val node = stack.pop()
            resultList.add(node.`val`)
            
            if (node.right != null) {
                stack.push(node.right!!)
                while(stack.peek().left != null) {
                    stack.push(stack.peek().left)
                }
            }
        }
        
        return resultList
        
    }
}
