fun longestIncreasingSubsequence(list: List<Int>) : List<Int> {

    val longestSubsequenceCountAtIndex = MutableList(list.size, {1})
    val subsequenceLink = MutableList(list.size, {-1})

    list.forEachIndexed({index, currentElement ->
        var maxSubsequenceLength = -1
        var predecessor = -1
        for (subIndex in 0 until index) {
            var subElement = list[subIndex]
            if (subElement < currentElement
                    && longestSubsequenceCountAtIndex[subIndex] + 1 > maxSubsequenceLength) {
                maxSubsequenceLength = longestSubsequenceCountAtIndex[subIndex] + 1
                predecessor = subIndex
                longestSubsequenceCountAtIndex[index] = maxSubsequenceLength
            }
        }

        if (maxSubsequenceLength != -1) {
            subsequenceLink[index] = predecessor
        }

    })

    return buildSequenceFromLink(subsequenceLink, list, getBiggestSubsequenceEndPosition(longestSubsequenceCountAtIndex))
}

fun getBiggestSubsequenceEndPosition(longestSubsequenceCountAtIndex: List<Int>) : Int {
    var max = Integer.MIN_VALUE
    var maxPosition = -1
    longestSubsequenceCountAtIndex.forEachIndexed { index, element ->
        if (element > max) {
            max = element
            maxPosition = index
        }
    }
    return maxPosition
}

fun buildSequenceFromLink(link: List<Int>, sequence: List<Int>, start: Int) : List<Int> {
    val increasingSequence = mutableListOf<Int>()
    var currentPosition = start
    while (currentPosition != -1) {
        increasingSequence.add(sequence[currentPosition])
        currentPosition = link[currentPosition]
    }
    return increasingSequence
}

fun main(args: Array<String>) {
    println(longestIncreasingSubsequence(listOf(0,-5, 7, 200, -2, 1, 0, 3, 2, 5, 0, 7, 9, 10, 300)))
}