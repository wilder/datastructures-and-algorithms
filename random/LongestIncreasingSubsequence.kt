import kotlin.test.assertEquals

/*
 * For each element in the list
 * count the length of the increasing subsequence at that position
 * and then get the biggest.
 *
 * @Return the longest increasing subsequence
 */
fun longestIncreasingSubsequence(list: List<Int>) : List<Int> {

    val longestSubsequenceCountAtIndex = MutableList(list.size, {1})

    var count = 1
    list.forEachIndexed { index, current ->
        if (index > 0 && list[index-1] < current) {
            count++
            longestSubsequenceCountAtIndex[index] = count
        } else {
            count = 1
        }
    }

    val maxCount =  longestSubsequenceCountAtIndex.max()!!
    return getSubsequenceFromMax(maxCount, list, longestSubsequenceCountAtIndex)!!
}

fun getSubsequenceFromMax(max: Int, list: List<Int>, countList: List<Int>) : List<Int>? {
    var lastStartPosition = 0
    countList.forEachIndexed({index, element ->
        if (element == max) {
            return list.subList(lastStartPosition, index + 1)
        } else if (element == 1) {
            lastStartPosition = index
        }
    })
    return null
}

fun main(args: Array<String>) {
    assertEquals(
            listOf(0,1,2,3,4,5,6,7,8,9),
            longestIncreasingSubsequence(listOf(1,2,3,4,1,2,0,1,2,3,4,5,6,7,8,9,0))
    )

    assertEquals(
            listOf(-2, -1, 0, 10, 100, 101),
            longestIncreasingSubsequence(listOf(1,2,3,4,-1,2,-2,-1,0,10,100,101,6,7,8,9,0))
    )

    assertEquals(
            listOf(10,20,30,31),
            longestIncreasingSubsequence(listOf(10,20,30,31,-1,2,3))
    )

    assertEquals(
            listOf(-1,2,3,10,20,30,31),
            longestIncreasingSubsequence(listOf(-1,2,3,10,20,30,31))
    )

}