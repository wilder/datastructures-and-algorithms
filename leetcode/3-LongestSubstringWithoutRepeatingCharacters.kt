/*
 * 3. Longest Substring Without Repeating Characters
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 */
class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        
        val seenCharacters = hashSetOf<Char>()
        var longestRangeSize = 0
        var initialIndex = 0
        var currentIndex = 0
        
        while (currentIndex < s.length) {
            val currentChar = s[currentIndex]
            if (!seenCharacters.contains(currentChar)) {
                seenCharacters.add(currentChar)
            } else {
                val currentRangeSize = currentIndex - initialIndex
                longestRangeSize = Math.max(currentRangeSize, longestRangeSize)
                var auxIndex = currentIndex-1
                var previousChar = s[auxIndex]
                while (previousChar != currentChar) {
                    auxIndex-=1
                    previousChar = s[auxIndex]
                }
                while (initialIndex < auxIndex) {
                    seenCharacters.remove(s[initialIndex])
                    initialIndex+=1
                }
                initialIndex+=1
            }
            currentIndex+= 1
        }
        
        val currentRangeSize = currentIndex - initialIndex
        return Math.max(currentRangeSize, longestRangeSize)
        
    }
}
