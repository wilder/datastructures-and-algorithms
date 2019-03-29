/*
 * 283. Move Zeroes
 * https://leetcode.com/problems/move-zeroes/submissions/
 */
class Solution {
    fun moveZeroes(nums: IntArray): Unit {

        var zeroesCount = 0
        var index = 0
        while(index < nums.size) {
            val currentValue = nums[index]

            if (currentValue == 0) {
                zeroesCount++
            } else if (zeroesCount > 0) {
                nums[index - zeroesCount] = currentValue
                nums[index] = 0
            }

            index += 1
        }

    }

}
