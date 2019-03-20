/**
 * 347. Top K Frequent Elements
 * https://leetcode.com/problems/top-k-frequent-elements/
 */
class Solution {
    fun topKFrequent(nums: IntArray, k: Int): List<Int> {

    val frequencyMap = mutableMapOf<Int, Int>()

    var maxCount = 0
    nums.forEach {
        val currentFrequency = frequencyMap.computeIfAbsent(it) {0} + 1
        maxCount = Math.max(maxCount, currentFrequency)
        frequencyMap.put(it, currentFrequency)
    }

    val groupedFrequencies = mutableMapOf<Int, MutableList<Int>>()

    frequencyMap.forEach { number, frequency ->
        groupedFrequencies.computeIfAbsent(frequency) {mutableListOf()}
            .add(number)
    }


    val topK = mutableListOf<Int>()

    var count = 0
    while (count < k) {
        if (groupedFrequencies.contains(maxCount)) {
            val numbers = groupedFrequencies[maxCount]!!
            while (!numbers.isEmpty()) {
                topK.add(numbers.get(numbers.size-1))
                numbers.removeAt(numbers.size-1)
                count++
            }
        }
        maxCount--
    }


    return topK
}

}
