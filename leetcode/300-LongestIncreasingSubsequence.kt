/*
 * 300. Longest Increasing Subsequence
 * https://leetcode.com/problems/longest-increasing-subsequence/
 */
class Solution {
    fun lengthOfLIS(nums: IntArray): Int {
        val longestIncreasingAtPosition = IntArray(nums.size) {1}
        var longest = 0
        
        for (i in 0 until nums.size) {
            var longestAtPosition = 1
            val currentElement = nums[i]
            for (j in i-1 downTo 0) {
                val pastElement = nums[j]
                if (currentElement > pastElement) {
                    longestAtPosition = Math.max(longestAtPosition, longestIncreasingAtPosition[j] + 1)
                }
            }
            longestIncreasingAtPosition[i] = longestAtPosition
            longest = Math.max(longest, longestAtPosition)
        }
        return longest
    }
}
