/**
 * 171. Excel Sheet Column Number
 * Daily Coding Problem - #212
 * https://leetcode.com/problems/excel-sheet-column-number/
 */
class Solution {
    fun titleToNumber(s: String): Int {
        val columnLimit = 26
        var columnNumber = 0
        var position = s.length - 1
        s.forEach {
            var multiplier = Math.pow(columnLimit.toDouble(), position.toDouble()).toInt()
            columnNumber += toNumber(it) * multiplier
            position -= 1
        }
        return columnNumber
    }
    
    fun toNumber(letter: Char): Int {
        return letter.toLowerCase() - 'a' + 1    
    }
    
}
