/**
 * 
 * 257. Binary Tree Paths
 * https://leetcode.com/problems/binary-tree-paths
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
    
    var paths: MutableList<String> = mutableListOf()
    
    fun binaryTreePaths(root: TreeNode?): List<String> {
        rootToLeafPaths(root, "")
        return paths
    }
    
    fun rootToLeafPaths(root: TreeNode?, currentPath: String) {
        
        if (root == null) {
            return
        }
        
        if (root.left == null && root.right == null) {
            paths.add(currentPath + root.`val`)
        }
        
        rootToLeafPaths(root.left, currentPath + "${root.`val`}->")
        rootToLeafPaths(root.right, currentPath + "${root.`val`}->")
        
    }
    
}
