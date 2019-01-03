/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
 */

import kotlin.test.assertEquals

fun Int?.safeInt(): Int {
    if (this == null)
        return 0
    return this
}

class TreeNode(val value: Char, var left: TreeNode? = null, var right: TreeNode? = null) {

    fun evaluate() : Int {
        // TODO: Refactor with polymorphism
        when(value) {
            // Handle division by 0?
            '/' -> return left?.evaluate().safeInt() / right?.evaluate().safeInt()
            '*' -> return left?.evaluate().safeInt() * right?.evaluate().safeInt()
            '+' -> return left?.evaluate().safeInt() + right?.evaluate().safeInt()
            '-' -> return left?.evaluate().safeInt() - right?.evaluate().safeInt()
            else -> return Integer.parseInt(value.toString())
        }
    }

}

fun evaluateExpression(root: TreeNode) : Int {
    return root.evaluate()
}

fun main(args: Array<String>) {
    val _3plus2 = TreeNode('+', TreeNode('3'), TreeNode('2'))
    assertEquals(5, evaluateExpression(_3plus2))

    val _4plus5 = TreeNode('+', TreeNode('4'), TreeNode('5'))
    assertEquals(9, evaluateExpression(_4plus5))

    val multiplication = TreeNode('*', _3plus2, _4plus5)
    assertEquals(45, evaluateExpression(multiplication))
}
