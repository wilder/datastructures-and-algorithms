import java.util.*

/**
 *
 * This problem was asked by Facebook.
 *
 * Given a string of round, curly, and square open and closing brackets,
 * return whether the brackets are balanced (well-formed).
 *
 * For example, given the string "([])[]({})", you should return true.
 * Given the string "([)]" or "((()", you should return false.
 *
 */

fun Char.isOpening() =
    this in mapOf('(' to true, '{' to true, '[' to true)

fun isBalanced(string: String): Boolean {
    val closeOpenMap = mapOf(')' to '(', '}' to '{', ']' to '[')
    val openCharQueue = LinkedList<Char>()
    for (char in string) {
        if (char.isOpening()) {
            openCharQueue.add(char)
        } else {
            if (!openCharQueue.isEmpty() && openCharQueue.removeLast() != closeOpenMap[char]) {
                return false
            }
        }
    }
    return openCharQueue.isEmpty()
}

fun main(args: Array<String>) {
    assert(isBalanced("([])[]({})"))
    assert(!isBalanced("([)]"))
    assert(!isBalanced("((()"))
    assert(!isBalanced("((()"))
}