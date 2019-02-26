/*
 * This problem was asked by Twitter.
 *
 * Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree
 *
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 *
 */
class LowestCommonAncestor {
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        if(root == null)
            return null;
        
        TreeNode ancestor = null;
        if (root.val == p.val || root.val == q.val)
            ancestor = root;
        
        TreeNode leftAncestor = lowestCommonAncestor(root.left, p, q);        
        TreeNode rightAncestor = lowestCommonAncestor(root.right, p, q);

        
        if (ancestor != null && ((rightAncestor != null) || (leftAncestor != null))) {
            return root;
        }
        
        if ((rightAncestor != null) && (leftAncestor != null)) {
            return root;
        }
        
        if(ancestor != null)
            return root;
        
        return leftAncestor != null ? leftAncestor : rightAncestor;
        
    }
    
}
