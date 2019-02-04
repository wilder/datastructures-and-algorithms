/*
This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

https://leetcode.com/problems/non-decreasing-array
*/

class Solution {
    fun checkPossibility(nums: IntArray): Boolean {
        return countNumbersOutOfOrderAndFix(nums) + countNumbersOutOfOrderAndFix(nums) <= 1
    }
    
    fun countNumbersOutOfOrderAndFix(nums: IntArray): Int {
        var modifications = 0
        for (i in 0 until nums.size - 1) {
            if (nums[i] > nums[i+1]) {
                modifications += 1
                if(i+2 < nums.size) {
                    if (nums[i+2] >= nums[i]) {
                        nums[i+1] = nums[i+2]
                    } else {
                        nums[i] = nums[i+1]
                    }
                } else {
                    nums[i+1] = nums[i]
                }
            }
        }
        return modifications
    }
}
