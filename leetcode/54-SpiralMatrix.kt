/*
 * 54. Spiral Matrix
 * https://leetcode.com/problems/spiral-matrix/
 *
*/
class Solution {
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {

    if (matrix.isEmpty()) {
        return listOf()
    }

    //Stores the pairs of directions for row, column
    //left->right, up->bottom, right->left, bottom->up
    val directions = listOf(Pair(0, 1), Pair(1, 0), Pair(0, -1), Pair(-1, 0))

    val numberOfElements = matrix.size * matrix[0].size
    var counter = 0 // 8

    val result = mutableListOf<Int>() //1, 2, 3, 6, 9, 8, 7, 4
    var row = 0 // 1
    var column = 0 // 0
    var direction = 0 // 0
    while (counter < numberOfElements) {

        if (!canVisit(row, column, matrix)) {
            row -= directions[direction].first
            column -= directions[direction].second
            if (direction == directions.size - 1) {
                direction = 0
            } else {
                direction++
            }
            row += directions[direction].first
            column += directions[direction].second
        }

        result.add(matrix[row][column])
        //marks as visited
        matrix[row][column] = -99999
        row += directions[direction].first
        column += directions[direction].second
        counter++

    }

    return result

}

    fun canVisit(row: Int, column: Int, matrix: Array<IntArray>): Boolean {
        return !isOutOfBounds(row, column, matrix) && !alreadyVisited(row, column, matrix)
    }

    fun isOutOfBounds(row: Int, column: Int, matrix: Array<IntArray>): Boolean {
        return row < 0 || row == matrix.size || column < 0 || column == matrix[0].size
    }

    fun alreadyVisited(row: Int, column: Int, matrix: Array<IntArray>): Boolean {
        return matrix[row][column] == -99999
    }
    
}
