/**
 *
 * 75. Sort Colors
 * https://leetcode.com/problems/sort-colors/
 *
 */
class Solution {

    /**
    * One-pass solution using offset for begin and end
    *
    * For each of the numbers, if current number is 0,
    * replace it with the number at begin offset position and increment offset
    *
    * if current number is 2, replace it with the end offset position and increment offset
    * if number is 1, ignore
    *
    */
   fun sortColors(nums: IntArray) {

      var beginOffSetPosition = 0
      var endOffSetPosition = nums.size

      var index = 0
      while (index < endOffSetPosition) {

          val value = nums[index]
          if (value == 0) {
              swap(nums, index, beginOffSetPosition)
              beginOffSetPosition++
          } else if (value == 2) {
              endOffSetPosition--
              swap(nums, index, endOffSetPosition)
              index--
          }

          index++
      }

    }

    private fun swap(nums: IntArray, index: Int, offSetPosition: Int) {
        val aux = nums[index]
        nums[index] = nums[offSetPosition]
        nums[offSetPosition] = aux
    }

    /**
     * 2 pass solution - Count sort like
     * Count number of each color and store on a array
     * Iterate the array construction the sorted output
     */
    fun sortColors2(nums: IntArray): Unit {

        val colorFrequencies = MutableList(3) {0}

        nums.forEach {
            colorFrequencies[it] += 1
        }

        var index = 0
        colorFrequencies.forEachIndexed { number, numberCount ->
            var counter = 0
            while (counter < numberCount) {
                nums[index] = number
                counter++
                index++
            }
        }


    }


}
