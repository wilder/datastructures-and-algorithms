/**
 *
 * 151. Reverse Words in a String
 * https://leetcode.com/problems/reverse-words-in-a-string/
 *
 */
class Solution {
    fun reverseWords(s: String): String {
        return s.split("\\s+".toRegex())
        .filter { a -> !a.isEmpty() }
        .reversed()
        .joinToString(" ")
    }
}
