/*
 * Populating Next Right Pointers in Each Node
 * https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
 *
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val,Node _left,Node _right,Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
    public Node connect(Node root) {
        connect(root, null);
        return root;
    }

    public void connect(Node root, Node next) {

        if (root == null) {
            return;
        }

        root.next = next;

        connect(root.left, root.right);
        connect(root.right, next == null ? null : next.left);

    }

}
