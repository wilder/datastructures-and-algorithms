/**
 * 617. Merge Two Binary Trees
 * https://leetcode.com/problems/merge-two-binary-trees
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
    fun mergeTrees(t1: TreeNode?, t2: TreeNode?): TreeNode? {
        
        if (t1 == null && t2 == null) {
            return null
        }
        
        var head: TreeNode? = null
        if (t1 != null && t2 != null) {
            head = TreeNode(t1.`val` + t2.`val`)
        } else if (t1 != null) {
             head = t1
        } else {
            head = t2
        }
        
        head!!.left = mergeTrees(t1?.left, t2?.left)
        head!!.right = mergeTrees(t1?.right, t2?.right)
        
        return head
        
    }
}
