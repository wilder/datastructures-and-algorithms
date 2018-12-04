import java.util.*
import kotlin.Comparator

/**
 * This problem was asked by Google.
 *
 * Given an array of integers and a number k, where 1 <= k <= length of the array,
 * compute the maximum values of each subarray of length k.
 *
 * For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
 * we should get: [10, 7, 8, 8], since:
 *
 * 10 = max(10, 5, 2)
 * 7 = max(5, 2, 7)
 * 8 = max(2, 7, 8)
 * 8 = max(7, 8, 7)
 *
 * Do this in O(n) time and O(k) space.
 * You can modify the input array in-place and you do not need to store the results.
 * You can simply print them out as you compute them.
 */

fun subArraysMax(array: List<Int>, subarrayLength: Int): List<Int> {

    val result = mutableListOf<Int>()
    val heap = PriorityQueue(subarrayLength, Comparator<Int> { o1, o2 -> o2.compareTo(o1) })
    var count = 1

    array.forEachIndexed {index, element ->
        heap.offer(element)
       if (count == subarrayLength) {
           result.add(heap.peek())
           val elementToBeRemoved = array[index+1 - count]
           heap.remove(elementToBeRemoved)
           count--
       }
       count++
    }

    return result
}

fun main(args: Array<String>) {
    assert(subArraysMax(listOf(10, 5, 2, 7, 8, 7), 3) == arrayOf(10, 7, 8, 8))
    assert(subArraysMax(listOf(10, 5, 2, 7, 8, 7), 2) == arrayOf(10, 5, 7, 8, 8))
    assert(subArraysMax(listOf(10, 5, 2, 7, 8, 7), 5) == arrayOf(10, 8))
}
