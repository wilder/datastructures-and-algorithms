/**
 * 33. Search in Rotated Sorted Array
 * https://leetcode.com/problems/search-in-rotated-sorted-array/
 */
 class Solution {
     fun search(nums: IntArray, target: Int): Int {
         val pivotIndex = searchPivot(nums, 0, nums.size - 1)
         if (pivotIndex == -1) {
             return binarySearch(nums, target, 0, nums.size - 1)
         } else {

             if(nums[pivotIndex] == target) {
                 return pivotIndex
             }

             if (target <= nums[nums.size - 1]) {
                 return binarySearch(nums, target, pivotIndex, nums.size - 1)
             }
             return binarySearch(nums, target, 0, pivotIndex - 1)
         }
     }

     /**
      * Searches for the pivot position
      * O(log n)
      */
     fun searchPivot(nums: IntArray, begin: Int, end: Int): Int {

         var begin = begin
         var end = end

         while (begin < end) {

             val mid = begin + (end - begin) / 2

             if (mid > begin && nums[mid-1] > nums[mid]) {
                 return mid
             } else if (mid < end && nums[mid+1] < nums[mid]) {
                 return mid + 1
             } else {
                 if (nums[begin] >= nums[mid]) {
                     end = mid -1
                 } else {
                     begin = mid + 1
                 }
             }
         }
         return -1
     }

     fun binarySearch(nums: IntArray, target: Int, begin: Int, end: Int): Int {

         var begin = begin
         var end = end

         while (begin <= end) {
             val mid = begin + (end - begin) / 2
             println("mid "+mid)
             if (target == nums[mid]) {
                 return mid
             }

             if (target > nums[mid]) {
                 begin = mid + 1
             } else {
                 end = mid - 1
             }

         }

         return -1
     }

 }
