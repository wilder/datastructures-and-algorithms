/*
 * This problem was asked by Twitter.
 *
 * Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree
 *
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 *
 */

class LowestCommonAncestor {

    public TreeNode lca = null;

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        traverse(root, p, q);
        return lca;
    }

    public boolean traverse(TreeNode root, TreeNode p, TreeNode q) {

        boolean isTarget = false;
        if (root.val == p.val || root.val == q.val) {
            isTarget = true;
        }

        boolean leftVisitedTarget = false;
        System.out.println("Visiting "+root.val);
        if(root.left != null) {
            leftVisitedTarget = traverse(root.left, p, q);
            System.out.println("Back to "+root.val + " from " + root.left.val + " leftVisitedTarget: " + leftVisitedTarget);
        }

        boolean rightVisitedTarget = false;
        if(root.right != null) {
            rightVisitedTarget = traverse(root.right, p, q);
            System.out.println("Back to "+root.val + " from " + root.right.val + " rightVisitedTarget: " + rightVisitedTarget);
        }

        if ((isTarget && (leftVisitedTarget||rightVisitedTarget))
             || (leftVisitedTarget && rightVisitedTarget) && lca == null) {
            System.out.println("I'm the LCA! "+ root.val);
            lca = root;
        }

        return isTarget || leftVisitedTarget || rightVisitedTarget;

    }

}
