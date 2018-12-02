import java.util.*

/**
 * This problem was asked by Google.
 *
 * You are given an M by N matrix consisting of booleans that represents a board.
 * Each True boolean represents a wall.
 * Each False boolean represents a tile you can walk on.
 *
 * Given this matrix, a start coordinate, and an end coordinate,
 * return the minimum number of steps required to reach the end coordinate from the start.
 *
 * If there is no possible path, then return null. You can move up, left, down, and right.
 *
 * You cannot move through walls. You cannot wrap around the edges of the board.
 *
 * For example, given the following board:
 *
 * [[f, f, f, f],
 * [t, t, f, t],
 * [f, f, f, f],
 * [f, f, f, f]]
 *
 * and start = (3, 0) (bottom left) and end = (0, 0) (top left), t
 * he minimum number of steps required to reach the end is 7,
 * since we would need to go through (1, 2)
 * because there is a wall everywhere else on the second row.
 */

fun isInBound(x: Int, y: Int, board: List<BooleanArray>): Boolean {
    return ( y >= 0 && y < board[0].size) && (x >=0 && x < board.size) && canWalkOn(y, x, board)
}

fun canWalkOn(x: Int, y: Int, board: List<BooleanArray>) =
    !board[x][y]

fun notVisited(position: Pair<Int, Int>?, visitedMap: MutableMap<Pair<Int, Int>, Boolean>) =
    !(position in visitedMap)

fun mapAdjacents(board: List<BooleanArray>): Map<Pair<Int, Int>, List<Pair<Int, Int>>> {

    val adjacents = mutableMapOf<Pair<Int, Int>, MutableList<Pair<Int, Int>>>()

    board.forEachIndexed { lineIndex, line ->
        line.forEachIndexed { colIndex, value ->
            val left = colIndex - 1
            val right = colIndex + 1
            val up = lineIndex - 1
            val down = lineIndex + 1
            if(canWalkOn(lineIndex, colIndex, board)) {
                if (isInBound(left, lineIndex, board))
                    adjacents.computeIfAbsent(Pair(lineIndex, colIndex),  {it -> mutableListOf() })
                        .add(Pair(lineIndex, left))
                if (isInBound(right, lineIndex, board))
                    adjacents.computeIfAbsent(Pair(lineIndex, colIndex),  {it -> mutableListOf() })
                        .add(Pair(lineIndex, right))
                if (isInBound(up, colIndex, board))
                    adjacents.computeIfAbsent(Pair(lineIndex, colIndex),  {it -> mutableListOf() })
                        .add(Pair(up, colIndex))
                if (isInBound(down, colIndex, board))
                    adjacents.computeIfAbsent(Pair(lineIndex, colIndex),  {it -> mutableListOf() })
                        .add(Pair(down, colIndex))
            }
        }
    }

    return adjacents
}

fun bfs(from: Pair<Int, Int>, to: Pair<Int, Int>, adjacents: Map<Pair<Int, Int>, List<Pair<Int, Int>>>): Int? {

    val visitedMap = mutableMapOf<Pair<Int, Int>, Boolean>()
    var distance = 0

    val children = LinkedList(adjacents[from])
    while (children.isNotEmpty()) {
        distance++
        val next = LinkedList<Pair<Int, Int>>()
        children.forEach {
            if (notVisited(it, visitedMap)) {
                visitedMap[it] = true
                if (it == to) {
                    return distance
                }
                if (it in adjacents) {
                    val nextChildren = adjacents[it]
                    next.addAll(nextChildren!!)
                }
            }
        }
        children.clear()
        children.addAll(next)
    }

    return null
}

fun closestPath(board: List<BooleanArray>, from: Pair<Int, Int>, to: Pair<Int, Int>): Int? {
    val adjacents = mapAdjacents(board)
    val minimumDistance = bfs(from, to, adjacents)
    return minimumDistance
}

fun main(args: Array<String>) {
    val board = listOf<BooleanArray>(
        booleanArrayOf(false, false, false, false),
        booleanArrayOf(true, true, false, true),
        booleanArrayOf(false, false, false, false),
        booleanArrayOf(false, false, false, false)
    )
    assert(closestPath(board, Pair(3,0), Pair(0,0)) == 7)
    assert(closestPath(board, Pair(1,2), Pair(0,0)) == 3)
}