/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86],
the maximum sum would be 137,
since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9],
the maximum sum would be 0,
since we would not take any elements.

Do this in O(N) time.

*/

import kotlin.math.max
import kotlin.test.assertEquals

fun maxContiguousSum(array: IntArray) : Int {

    var maxSum = 0
    var currentSum = 0

    for (element in array) {
        currentSum = max(element, currentSum + element)
        maxSum = max(maxSum, currentSum)
    }

    return maxSum
}

fun main(args: Array<String>) {
    assertEquals(maxContiguousSum(intArrayOf()), 0)
    assertEquals(maxContiguousSum(intArrayOf(-5, -1, -8, -9)), 0)
    assertEquals(maxContiguousSum(intArrayOf(34, -50, 42, 14, -5, 86)), 137)
}
