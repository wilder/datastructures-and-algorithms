/**
 * 200. Number of Islands
 * https://leetcode.com/problems/number-of-islands/
 */
import java.util.*
class Solution {

    lateinit var adjacents: Map<Pair<Int, Int>, List<Pair<Int, Int>>>
    lateinit var grid: Array<CharArray>

    fun numIslands(grid: Array<CharArray>): Int {

        if (grid.isEmpty()) {
            return 0
        }

        this.grid = grid
        this.adjacents = mapAdjacents(grid)

        return countIslands()
    }

    fun mapAdjacents(grid: Array<CharArray>): Map<Pair<Int, Int>, List<Pair<Int, Int>>>{
        val adjacents = mutableMapOf<Pair<Int, Int>, MutableList<Pair<Int, Int>>>()
        val lineCount = grid.size
        val columnCount = grid[0].size

        for(line in 0 until grid.size) {
            for (column in 0 until grid[line].size) {
                val current = Pair(line, column)
                if (isIsland(current)) {
                    val up = Pair(line - 1, column)
                    val right = Pair(line, column + 1)
                    val left = Pair(line, column - 1)
                    val down = Pair(line + 1, column)

                    listOf(up, right, left, down)
                        .filter {isInBounds(it, lineCount, columnCount) && isIsland(it)}
                        .map { adj -> adjacents
                            .computeIfAbsent(current, { mutableListOf()})
                            .add(adj)
                        }
                }
            }
        }
        return adjacents
    }

    fun isInBounds(coordinates: Pair<Int, Int>, lineCount: Int, columnCount: Int): Boolean {
        val line = coordinates.first
        val column = coordinates.second
        return line >= 0 && line < lineCount && column >= 0 && column < columnCount
    }

    fun isIsland(coordinates: Pair<Int, Int>) = grid[coordinates.first][coordinates.second] == '1'

    fun countIslands(): Int {
        var numberOfIslands = 0
        for (line in 0 until grid.size) {
            for (column in 0 until grid[line].size) {
                val position = Pair(line, column)
                if (notVisited(position) && isIsland(position)) {
                    visit(position)
                    numberOfIslands++
                }
            }
        }
        return numberOfIslands
    }

    fun notVisited(position: Pair<Int, Int>) = grid[position.first][position.second] != 'x'

    fun visit(position: Pair<Int, Int>) {

        grid[position.first][position.second] = 'x'

        adjacents[position]
            ?.filter { notVisited(it) }
            ?.forEach { visit(it) }

    }
}
