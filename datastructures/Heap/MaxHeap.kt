package priorityQueue.heap

import safeInt

class MaxHeap(inputArray: List<Int>) : Heap {

    var array = inputArray.toMutableList()

    init {
        buildMaxHeap(array)
    }


    override fun max(): Int {
        return array[0]
    }


    /**
     * Time Complexity: O(log n)
     **/
    override fun extractMax(): Int {
        swap(0, array.size-1)
        val max = array.removeAt(array.size - 1)
        if (!array.isEmpty())
            maxHeapfy(0)
        return max
    }

    /**
     * Turns the array into a max heap by running
     * maxHeapfy starting from the leaves and going up
     *
     *
     * Time complexity: O(n) Explanation:
     *
     * When looking at the n/2 node there are only the max of 2 operation to be done
     * (Constant number of operations).
     *
     * Observe maxHeapfy takes constant time for nodes that are onle level above the leaves,
     * in general, O(l) time, for nodes that are l levels above the leaves.
     *
     * n/4 nodes with level 1, n/8 with level 2, ... 1 node log n level (root)
     *
     * Total amount of work in the for-loop
     * n/4 * (1*c) + n/8 * (2*c) + ... 1(logn * c)
     *
     */
    override fun buildMaxHeap(array: List<Int>) {
        for (index in array.size / 2 downTo 0) {
            maxHeapfy(index)
        }
    }

    /**
     * If the max heap property if violated (if max is not the current index)
     * exchange the max value with the current and run maxHeapfy for the exchanged index
     * until the heap property is not violated
     *
     * Time Complexity: O(log n)
     */
    override fun maxHeapfy(index: Int) {
        return maxHeapfy(index, false)
    }

    override fun insert(element: Int) {
        array.add(element)
        val index = getParentIndex(array.size - 1)
        return maxHeapfy(index, true)
    }

    private fun maxHeapfy(index: Int, insertion: Boolean) {

        val current = array[index]
        val left = getLeft(index)
        val right = getRight(index)

        val maxIndexAndValue = getMax(index, left, right)
        val maxIndex = maxIndexAndValue.first
        val max = maxIndexAndValue.second

        if (max == current)
            return

        // the max heap property is violated
        // exchange with the max
        swap(index, maxIndex)

        return if (insertion) {
            maxHeapfy(getParentIndex(index), insertion)
        } else {
            maxHeapfy(maxIndex, insertion)
        }

    }

    /**
     * Return the max value among the three as an Pair of
     * the index and the value
     */
    private fun getMax(current: Int, left: Int?, right: Int?): Pair<Int, Int> {
        val currentVal = array[current]

        val leftVal: Int = getValue(left).safeInt(Integer.MIN_VALUE)
        val rightVal: Int = getValue(right).safeInt(Integer.MIN_VALUE)

        if (currentVal >= leftVal && currentVal >= rightVal) {
            return Pair(current, currentVal)
        } else if (leftVal >= rightVal) {
            return Pair(left.safeInt(), leftVal)
        } else {
            return Pair(right.safeInt(), rightVal)
        }

    }

    private fun getValue(index: Int?): Int? {
        if (index == null)
            return null
        if (index < 0 || index >= array.size)
            return null
        return array[index]
    }

    private fun swap(index: Int, otherIndex: Int) {
        val aux = array[otherIndex]
        array[otherIndex] = array[index]
        array[index] = aux
    }

    fun isEmpty() = array.isEmpty()

    private fun getParentIndex(index: Int): Int {
        return index / 2
    }

    private fun getLeft(index: Int): Int? {
        val leftIndex = index * 2 + 1
        if (leftIndex >= array.size ) {
            return null
        }
        return leftIndex
    }

    private fun getRight(index: Int): Int? {
        val rightIndex = index * 2 + 2
        if (rightIndex >= array.size) {
            return null
        }
        return rightIndex
    }

}

/**
 * Time complexity: O(n log n) 
 */
fun heapSort(array: List<Int>): List<Int> {
    val sorted = mutableListOf<Int>()
    val maxHeap = MaxHeap(array)

    while (!maxHeap.isEmpty())
        sorted.add(maxHeap.extractMax())

    return sorted.toList()

}

fun Int?.safeInt(defaultValue: Int = 0): Int {
    if (this == null)
        return defaultValue
    return this
}

fun main(args: Array<String>) {
    print(heapSort(listOf(9, 1, 5, 10, 4, -200, -100, -305, 0, 7, 300)))
}
