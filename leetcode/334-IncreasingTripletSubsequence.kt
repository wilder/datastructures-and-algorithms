/*
 * 334. Increasing Triplet Subsequence
 * https://leetcode.com/problems/increasing-triplet-subsequence/
 */
class Solution {
    fun increasingTriplet(nums: IntArray): Boolean {
        
        if (nums.size < 3) {
            return false
        }
        
        var smallest = nums[0]
        var secondSmallest = -1
        
         nums.forEach {
            if (secondSmallest != -1 && it > secondSmallest) {
                return true
            }
            
            if (it < smallest) {
                smallest = it
            } else if (it > smallest) {
                if (secondSmallest == -1) {
                    secondSmallest = it
                } else {
                    secondSmallest = Math.min(secondSmallest, it)   
                }
            }
            
            
        }
        
        return false
    }
}
