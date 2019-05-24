/**
 * 125. Valid Palindrome
 * https://leetcode.com/problems/valid-palindrome/
 *
 */
class Solution {
    
    fun Char.isAlphanumeric(): Boolean = this.isDigit() || this.isLetter()
    
    fun isPalindrome(s: String): Boolean {
            
        var beginIndex = 0
        var endIndex = s.length - 1

        while (beginIndex < endIndex) {
            
            if (!s[beginIndex].isAlphanumeric()) {
                beginIndex++
                continue
            }
            
            if (!s[endIndex].isAlphanumeric()) {
                endIndex--
                continue
            }
            
            if (s[beginIndex].toLowerCase() != s[endIndex].toLowerCase()) {
                return false
            }
            
            beginIndex++
            endIndex--
        }
        
        return true
        
    }
}
