/**
 * 17. Letter Combinations of a Phone Number
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 */
class Solution {

    val digitLetters = listOf(
        emptyList(),
        emptyList(),
        listOf('a', 'b', 'c'),
        listOf('d', 'e', 'f'),
        listOf('g', 'h', 'i'),
        listOf('j', 'k', 'l'),
        listOf('m', 'n', 'o'),
        listOf('p', 'q', 'r', 's'),
        listOf('t', 'u', 'v'),
        listOf('w', 'x', 'y', 'z')
    )

    fun letterCombinations(digits: String): List<String> {

        var combinations = listOf<String>()

        digits.forEach {
            val letters = digitLetters[it.toString().toInt()]

            if (combinations.isEmpty()) {
                combinations = letters.map {it.toString()}
            } else {
                combinations = combinations.flatMap {
                    combination -> letters.map { combination + it }
                }
            }
        }

        return combinations
    }

}
