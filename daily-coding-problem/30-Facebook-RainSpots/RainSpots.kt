/**
 * This problem was asked by Facebook.
 *
 * You are given an array of non-negative integers that represents a two-dimensional elevation map
 * where each element is unit-width wall and the integer is the height.
 *
 * Suppose it will rain and all spots between two walls get filled up.
 *
 * Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
 *
 * For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
 *
 * Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index,
 * 2 in the second, and 3 in the fourth index
 * (we cannot hold 5 since it would run off to the left),
 * so we can trap 8 units of water.
 *
 */


/**
 * Time Complexity O(n)
 * Space Complexity O(n)
 */
fun countUnitsOfWater(elevationMap: List<Int>): Int {
    // Store the values of the highest wall on the left of each element
    val highestWallsOnLeft = MutableList(elevationMap.size, {0})
    highestWallsOnLeft[0] = elevationMap[0]
    for (index in 1 until  elevationMap.size) {
        highestWallsOnLeft[index] = Math.max(highestWallsOnLeft[index-1], elevationMap[index])
    }

    // Store the values of the highest wall on the right of each element
    val highestWallsOnRight = MutableList(elevationMap.size, {0})
    highestWallsOnRight[elevationMap.size-1] = elevationMap[elevationMap.size-1]
    for (index in elevationMap.size-2 downTo 0) {
        highestWallsOnRight[index] = Math.max(highestWallsOnRight[index+1], elevationMap[index])
    }

    var unitsOfWater = 0
    elevationMap.forEachIndexed {
        index, elevation -> unitsOfWater += Math.min(highestWallsOnLeft[index], highestWallsOnRight[index]) - elevation
    }

    return unitsOfWater
}

fun main(args: Array<String>) {
    println(countUnitsOfWater(listOf(2, 1, 2))) // 1
    println(countUnitsOfWater(listOf(3, 0, 1, 2, 3))) // 6
    println(countUnitsOfWater(listOf(5,2,4,1))) // 2
    println(countUnitsOfWater(listOf(1,2,4,5))) //0
    println(countUnitsOfWater(listOf(5,4,3,2))) // 0
}
