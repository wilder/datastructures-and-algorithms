/*
 * 55. Jump Game
 * https://leetcode.com/problems/jump-game/submissions/
 */
class Solution {

    fun canJump(nums: IntArray): Boolean {

        val memo = MutableList<Boolean>(nums.size) {false}
        memo[nums.size - 1] = true

        var index = nums.size - 2

        while (index >= 0) {
            memo[index] = canReach(index, nums, memo)
            index -= 1
        }

        return memo[0]

    }

    /*
     * Can be improved by updating the target position every time it can reach the target. Then, only check if the current jump is greater than the target.
     */
    fun canReach(index: Int, nums: IntArray, memo: List<Boolean>): Boolean {
        for (jump in 0..nums[index]) {
            if (jump >= nums.size-1) {
                return true
            } else {
                val canReachFromCurrent = memo[index + jump]
                if (canReachFromCurrent) {
                    return true
                }
            }
        }
        return false
    }

}
