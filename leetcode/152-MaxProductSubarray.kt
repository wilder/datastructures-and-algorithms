/**
 *
 * 152. Maximum Product Subarray
 * https://leetcode.com/problems/maximum-product-subarray/
 *
 */
class Solution {
    fun maxProduct(nums: IntArray): Int {
        
        var currentMax = nums[0]
        var previousMax = nums[0]
        var previousMin = nums[0]
        var maxProduct = nums[0]
        
        for (i in 1 until nums.size) {
            val currentValue = nums[i]
            currentMax = Math.max(currentValue, Math.max(currentValue * previousMax, currentValue * previousMin))
            previousMin = Math.min(currentValue, Math.min(currentValue * previousMax, currentValue * previousMin))
            maxProduct = Math.max(maxProduct, currentMax)
            previousMax = currentMax
        }
        
        
        return Math.max(maxProduct, currentMax)
    }
}
