/*
 * 55. Jump Game
 * https://leetcode.com/problems/jump-game/submissions/
 */
class Solution {
    
    fun canJump(nums: IntArray): Boolean {
        
        var targetPosition = nums.size - 1 
        
        var index = nums.size - 2
        
        while (index >= 0) {
            val jumpLength = nums[index]
            
            if (jumpLength + index >= targetPosition) {
                targetPosition = index
            }
            
            index -= 1
        }
        
        return targetPosition == 0
                       
    }
    
}
