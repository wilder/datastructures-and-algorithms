/**
 * 22. Generate Parentheses
 * https://leetcode.com/problems/generate-parentheses/
 */
class Solution {

    val combinations = mutableListOf<String>()

    fun generateParentheses(n: Int): List<String> {
        generateParentheses(n, n, "")
        return combinations
    }

    private fun generateParentheses(open: Int, closed: Int, combination: String) {
        if (open == 0 && closed == 0) {
            combinations.add(combination)
        } else {
            if (open > 0) {
                generateParentheses(open - 1, closed, "$combination(")
            }
            if (closed > 0 && closed > open) {
                generateParentheses(open, closed - 1, "$combination)")
            }
        }
    }


    //works but not in leetcode's desired order
    fun generateParenthesesIterative(n: Int): List<String> {

        if (n == 0) {
            return listOf("")
        }

        /**
         * add parentheses from left side, right side and around
         * for each of the current combinations
         */

        var combinations = setOf("()")
        var count = 1

        while(count < n) {
            combinations = combinations.flatMap {
                linkedSetOf("($it)", "$it()", "()$it")
            }.toSet()
            count++
        }

        return combinations.toList()
    }



}
