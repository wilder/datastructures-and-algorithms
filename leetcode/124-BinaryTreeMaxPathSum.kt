/**
 *
 * Binary Tree Maximum Path Sum
 * https://leetcode.com/problems/binary-tree-maximum-path-sum
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
    
    var max = Integer.MIN_VALUE //3
    
    fun maxPathSum(root: TreeNode?): Int {
        val maxPath = maxPathSumHelper(root)
        return Math.max(max, maxPath)
    }
    
    fun maxPathSumHelper(root: TreeNode?): Int {
        
        if (root == null) {
            return 0
        }
        
        val leftMaxPath = maxPathSumHelper(root.left)
        val rightMaxPath = maxPathSumHelper(root.right)
        
        val currentAndRight = root.`val` + rightMaxPath
        val currentAndLeft = root.`val` + leftMaxPath
        
        var currentMax = Math.max(root.`val`, Math.max(currentAndRight, currentAndLeft))
        
        val fullPath = root.`val` + leftMaxPath + rightMaxPath
        this.max = Math.max(currentMax, Math.max(max, fullPath))
        
        return currentMax
        
    }
}
