import java.lang.Math.max
import kotlin.test.assertTrue

/*
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
*/

/**
 * Multiplies the biggest three numbers and the lowest 2 numbers 
 * with the greatest and returns the biggest value
 */
fun maxProduct(list: List<Int>): Int {
    val sortedList = list.sortedDescending()
    return max(sortedList[0] * sortedList[1] * sortedList[2],
        sortedList[sortedList.lastIndex] * sortedList[sortedList.lastIndex - 1] * sortedList[0])
}


fun main(args: Array<String>) {
    assertTrue { maxProduct(listOf(-10, -10, 5, 2)) == 500}
    assertTrue { maxProduct(listOf(-1, 100, -450, 4)) == 45000}
    assertTrue { maxProduct(listOf(1000, 100, -4500, 234)) == 23400000}
}
