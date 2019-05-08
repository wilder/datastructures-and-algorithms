/*
 * 62. Unique Paths
 * https://leetcode.com/problems/unique-paths/
 */
class Solution {
    /*
     * Bottom-up Solution
     * Starts at the final position and set the value for UniquePaths = 1
     * For each of the other cells starting from the final position,
     * set the current cell value to the sum of the UniquePaths for the cell above and at left
     * return the Start cell value
     */
    fun uniquePaths(m: Int, n: Int): Int {
        //bottom-up solution
        val matrix = MutableList<IntArray>(m) {IntArray(n) {0}} 
        matrix[0][0] = 1
        
        matrix.forEachIndexed { lineIndex, line -> 
            line.forEachIndexed { columnIndex, column ->
                var uniquePaths = 0
                if (lineIndex -1 >= 0) {
                    uniquePaths += matrix[lineIndex-1][columnIndex]
                }
                
                if (columnIndex -1 >= 0) {
                    uniquePaths += matrix[lineIndex][columnIndex-1]
                }
                
                matrix[lineIndex][columnIndex] += uniquePaths
            }
        }
        
        return matrix[matrix.size - 1][matrix[0].size - 1]
    }
}
