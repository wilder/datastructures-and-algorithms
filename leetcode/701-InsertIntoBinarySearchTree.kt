/**
 *
 * 701. Insert into a Binary Search Tree
 * https://leetcode.com/problems/insert-into-a-binary-search-tree/
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
    fun insertIntoBST(root: TreeNode?, `val`: Int): TreeNode? {
        
        if (root == null) {
            return null
        }
        
        if (`val` < root.`val`) {
            //go to left
            if (root!!.left == null) {
                root.left = TreeNode(`val`)
            } else {
                root.left = insertIntoBST(root.left, `val`)
            }
        } else {
            if (root!!.right == null) {
                root.right = TreeNode(`val`)
            } else {
                root.right = insertIntoBST(root.right, `val`)
            }
        }
        
        return root
    }
}
