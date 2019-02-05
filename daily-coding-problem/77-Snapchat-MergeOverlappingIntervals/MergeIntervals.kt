import kotlin.test.assertEquals

/*
 * This problem was asked by Snapchat.
 * 
 * Given a list of possibly overlapping intervals
 * return a new list of intervals where all overlapping intervals have been merged.
 *
 *  The input list is not necessarily ordered in any way.
 *  
 *  For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], 
 *  you should return [(1, 3), (4, 10), (20, 25)]
 *  
 *  https://leetcode.com/problems/merge-intervals
 * 
 */

data class Interval(
    var start: Int = 0,
    var end: Int = 0
)


class MergeIntervals {
    fun merge(intervals: List<Interval>): List<Interval> {

        if (intervals.isEmpty()) {
            return emptyList()
        }

        val sortedIntervals = intervals.sortedBy { it.start }

        var mergedInterval = sortedIntervals.get(0)
        val mergedIntervals = mutableListOf<Interval>()

        for (i in 1 until sortedIntervals.size) {
            val currentInterval = sortedIntervals[i]
            if (currentInterval.start > mergedInterval.end) {
                mergedIntervals.add(mergedInterval)
                mergedInterval = currentInterval
            } else if (currentInterval.end > mergedInterval.end) {
                mergedInterval.end = currentInterval.end
            }
        }

        mergedIntervals.add(mergedInterval)
        return mergedIntervals

    }
}

fun main(args: Array<String>) {
    assertEquals(
        listOf(Interval(1, 6), Interval(8, 10), Interval(15, 18)),
        MergeIntervals().merge(listOf(Interval(1, 3), Interval(8, 10), Interval(2, 6), Interval(15, 18)))
    )
}
